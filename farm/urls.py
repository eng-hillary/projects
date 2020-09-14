from django.urls import include, path
from rest_framework import routers
from . import views
from .views import SectorList, SectorDetail, CreateSector,EnterpriseList




router = routers.DefaultRouter()
<<<<<<< HEAD
router.register(r'farms', views.SectorViewSet)
router.register(r'farms', views.EnterpriseViewSet)
=======
router.register(r'sector', views.SectorViewSet)
router.register(r'enterprise', views.EnterpriseViewSet)
>>>>>>> 80d82ddd3d57a564901efc611a3b0d8a79fd6dc8

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'farms'
urlpatterns = [
    path('', include(router.urls)),
    path('sectors', SectorList.as_view(), name='sector_list'),
    path('<int:pk>/edit/sector', SectorDetail.as_view(), name="edit_sector"),
    path('create/sector', CreateSector.as_view(), name="create_sector"),
    path('enterprises', EnterpriseList.as_view(), name='enterprise_list'),
]
