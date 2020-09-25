
from django.urls import include, path
from rest_framework import routers
from . import views
from .views import (GroupList, FarmerProfileList, CreateFarmerProfile, UpdateFarmerProfile)


router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'farmerprofiles', views.FarmerProfileViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'farmer'
urlpatterns = [
    path('', include(router.urls)),
    path('groups', GroupList.as_view(), name='group_list'),
    path('farmerprofile', FarmerProfileList.as_view(), name='farmerprofile_list'),
    path('create/profile', CreateFarmerProfile.as_view(), name="create_farmer"),
    path('<int:pk>/edit/', UpdateFarmerProfile.as_view(), name="edit_farmer_profile"),

]
