
from .models import CommunityWeather
from django.contrib.gis import forms 
from django.contrib.gis.geos import Point


class WeatherForm(forms.ModelForm):
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}),
    initial=Point(x=0.2507599 , y=32.5780179, srid=4326))

  
    class Meta:
        model = CommunityWeather
        exclude = ['date_reported','reported_by','time_reported']

    def __init__(self, *args, **kwargs):
        super(WeatherForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '1'})

   