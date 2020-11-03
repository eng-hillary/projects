from django.urls import include, path
from rest_framework import routers
from . import views
from .views import CommunityWeatherList 


router = routers.DefaultRouter()
router.register(r'community_weather', views.CommunityWeatherViewSet)

app_name = 'weather'
urlpatterns = [
    path('api/', include(router.urls)),
    path('communityweather', CommunityWeatherList.as_view(), name='communityweather_list'),
]
