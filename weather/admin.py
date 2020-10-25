from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import CommunityWeather
@admin.register(CommunityWeather)

class WeatherAdmin(OSMGeoAdmin):
    list_display = [
        'weather',
        'region',
        'district',
        'county',
        'sub_county',
        'parish',
        'village'
        ]
