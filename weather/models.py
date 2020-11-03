from django.db import models
from common .models import TimeStampedModel
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from geopy.geocoders import Nominatim

# Create your models here.

class CommunityWeather(TimeStampedModel, models.Model):
    WEATHER_CHOICES=(
        (
        None, "--please select--"),
        ('clear_sky','Clear sky'),
        ('few_clouds','Few clouds'),
        ('scattered_clouds','Scattered clouds'),
        ('broken_clouds','Broken clouds'),
        ('shower_rain','Shower rain'),
        ('rain','Rain'),
        ('thunderstorm','Thunderstorm'),
        ('snow','Snow'),
        ('mist','Mist')
    )
    
    weather = models.CharField(max_length=50,choices=WEATHER_CHOICES, null=False, blank=False)
    date_reported = models.DateTimeField(auto_now=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weather_agent')
    description = models.TextField(null=False, blank=False)
    #location of person reporting weather
    lat = models.FloatField(_('Latitude'), blank=True, null=True, help_text="Latitude of your location")
    lon = models.FloatField(_('Longitude'), blank=True, null=True,help_text="Longitude of your location")


    def __str__(self):
        return self.weather

    @property
    def compute_location(self):
        geolocator = Nominatim(user_agent="ICT4Farmers", timeout=10)
        lat = str(self.lat)
        lon = str(self.lon)
       
        try:

            location = geolocator.reverse(lat + "," + lon)
            return '{}'.format(location.address)
        except:
            location = str(self.lat) + "," + str(self.lon)
            return 'slow network, loading location ...'