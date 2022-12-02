from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from .models import Place, Image



def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = place.images.all()
    place_info = {
    "title": place.title,
    "imgs": [image.picture.url for image in images],
    "description_short": place.description_short,
    "description_long": place.description_long,
    "coordinates": {
        "lat": place.lat,
        "lng": place.lng,
      }
     }
    
    return JsonResponse(place_info, content_type='application/json')
