from django.db import models
from common .models import TimeStampedModel
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from common .models import Region,County,SubCounty, Parish, Village, District
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
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=False, null=True)
    county = models.ForeignKey(County,  on_delete=models.CASCADE, null=True, blank=False)
    sub_county = models.ForeignKey(SubCounty,on_delete=models.CASCADE, blank=False, null=True)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE, blank=False, null=True)
    village = models.ForeignKey(Village,on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.weather