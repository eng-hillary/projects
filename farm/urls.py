from django.urls import include, path
from rest_framework import routers
from . import views
from .views import SectorList, SectorDetail, CreateSector


router = routers.DefaultRouter()
router.register(r'farms', views.SectorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'farms'
urlpatterns = [
    path('', include(router.urls)),
    path('sectors', SectorList.as_view(), name='sector_list'),
    path('<int:pk>/edit/sector', SectorDetail.as_view(), name="edit_sector"),
     path('create/sector', CreateSector.as_view(), name="create_sector"),
]