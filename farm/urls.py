from django.urls import include, path
from rest_framework import routers
from . import views
from .views import (SectorList, SectorDetail, CreateSector,EnterpriseList, FarmListView, FarmViewSet, 
CreateFarmView, EditFarmView,FarmMapViewSet,CreateEnterpriseView)




router = routers.DefaultRouter()

router.register(r'farms', views.FarmViewSet,'farm-api')
router.register(r'maps', views.FarmMapViewSet,'maps-api')
router.register(r'sector', views.SectorViewSet,'apisector')
router.register(r'enterprise', views.EnterpriseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'farm'
urlpatterns = [
    path('api/', include(router.urls)),
    path('list', FarmListView.as_view(), name='farm_list'),
    path('create', CreateFarmView.as_view(), name="create_farm"),
    path('sectors', SectorList.as_view(), name='sector_list'),
    path('<int:pk>/edit/farm', EditFarmView.as_view(), name="edit_farm"),
    path('<int:pk>/edit/sector', SectorDetail.as_view(), name="edit_sector"),
    path('create/sector', CreateSector.as_view(), name="create_sector"),
    path('enterprises', EnterpriseList.as_view(), name='enterprise_list'),
    path('create/enterprise/<int:farm_pk>', CreateEnterpriseView.as_view(), name="create_enterprise"),
    
]
