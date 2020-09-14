from rest_framework import serializers
from .models import CommunityWeather
from django.contrib.auth.models import User

class CommunityWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityWeather 
        fields = ('latitude', 'longitude', 'weather', 'date_reported', 'reported_by', 'general_remarks')