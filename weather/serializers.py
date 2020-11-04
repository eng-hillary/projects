from rest_framework import serializers
from .models import CommunityWeather
from django.contrib.auth.models import User

class CommunityWeatherSerializer(serializers.ModelSerializer):
    village = serializers.CharField(source='compute_location',required=False, read_only=True)
    reported_by = serializers.SerializerMethodField(method_name='get_weather_agent',source='reported_by')
    date_reported = serializers.DateField(format='%d-%m-%Y')
    time_reported = serializers.TimeField(format='%H:%M')

    class Meta:
        model = CommunityWeather 
        fields = ['id','weather','village','reported_by','date_reported','time_reported','description','lon','lat']
    

    def get_weather_agent(self, obj):
        return '{} {}'.format(obj.reported_by.first_name, obj.reported_by.last_name)


class PostWeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityWeather 
        fields = ['weather','description','lon','lat']
    
