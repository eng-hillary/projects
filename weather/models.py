from django.db import models
from common .models import TimeStampedModel
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
# Create your models here.

class CommunityWeather(TimeStampedModel, models.Model):
    latitude = models.FloatField(_('Latitude'), blank=True, null=True)
    longitude = models.FloatField(_('Longitude'), blank=True, null=True)
    weather = models.CharField(max_length=100, null=False, blank=False)
    date_reported = models.DateTimeField(auto_now=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='weather_agent')
    general_remarks = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.weather