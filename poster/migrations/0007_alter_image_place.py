# Generated by Django 4.1.3 on 2022-12-08 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0006_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='poster.place', verbose_name='локация'),
        ),
    ]
