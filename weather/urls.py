from django.urls import include, path
from rest_framework import routers
from . import views
from .views import CommunityWeatherList 


router = routers.DefaultRouter()
router.register(r'communityweather', views.CommunityWeatherViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'weather'
urlpatterns = [
    path('', include(router.urls)),
    path('communityweather', CommunityWeatherList.as_view(), name='communityweather_list'),
]
