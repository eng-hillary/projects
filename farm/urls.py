from django.urls import include, path
from rest_framework import routers
from . import views
from .views import SectorList, EnterpriseList


router = routers.DefaultRouter()
router.register(r'farms', views.SectorViewSet)
router.register(r'farms', views.EnterpriseList)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'farms'
urlpatterns = [
    path('', include(router.urls)),
    path('sectors', SectorList.as_view(), name='sector_list'),
    path('enterprises', EnterpriseList.as_view(), name='enterprise_list'),
]