from rest_framework import serializers
from .models import CommunityWeather
from django.contrib.auth.models import User

class CommunityWeatherSerializer(serializers.ModelSerializer):
    village = serializers.CharField(source='compute_location')
    class Meta:
        model = CommunityWeather 
        fields = ['id','weather','village']