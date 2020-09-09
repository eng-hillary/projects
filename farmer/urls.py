<<<<<<< HEAD
=======
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import GroupList, FarmerProfileList


router = routers.DefaultRouter()
router.register(r'farmer', views.GroupViewSet)
router.register(r'farmer', views.FarmerProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'farmer'
urlpatterns = [
    path('', include(router.urls)),
    path('groups', GroupList.as_view(), name='group_list'),
    path('farmerprofile', FarmerProfileList.as_view(), name='farmerprofile_list'),

]
>>>>>>> 4136e3c639cef14ee456535c2b845b10dce68e07
