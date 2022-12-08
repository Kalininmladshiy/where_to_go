import requests
import os
import time
import json
from pathlib import Path
from django.core.files import File
from django.core.management.base import BaseCommand
from poster.models import Place, Image


def get_filenames(path):
    filenames = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            filenames.append(filename)
    return filenames

def download_file(path, url):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)    
    

class Command(BaseCommand):

    def handle(self, *args, **options):
        path = Path.cwd() / 'static' / 'places'
        filenames = get_filenames(path)
        for filename in filenames:
            with open(os.path.join(Path.cwd() / 'static' / 'places', filename), "r") as file:
                place_json = file.read()
            place = json.loads(place_json)
            new_place = Place.objects.get_or_create(
                title=place['title'],
                description_short=place['description_short'],
                description_long=place['description_long'],
                lng=place['coordinates']['lng'],
                lat=place['coordinates']['lat'],
             )
            for num, img in enumerate(place['imgs'], 1):
                img_filename = f"{num}_{place['title']}.jpg"
                url = img
                try:
                    download_file(img_filename, url)
                except requests.exceptions.ConnectionError:
                    print('Произошел разрыв сетевого соединения. Ожидаем 10 секунд.')
                    time.sleep(10)
                    continue
                except requests.exceptions.HTTPError:
                    print('Что-то с адресом страницы')
                    continue
                img = Image()
                img.picture.save(img_filename, File(open(Path.cwd() / img_filename, 'rb')), save=True)
                new_place[0].images.add(img)
                os.remove(img_filename)


if __name__ == "__main__":
    Command().handle()