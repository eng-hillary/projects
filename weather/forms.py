
from django import forms
from .models import CommunityWeather



class WeatherForm(forms.ModelForm):
  
    class Meta:
        model = CommunityWeather
        exlude = ['date_reported','reported_by']

    def __init__(self, *args, **kwargs):
        super(WeatherForm, self).__init__(*args, **kwargs)

   