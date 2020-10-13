from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ResourceList,CreateResourceView,EditResourceView,ResourceSharingList, ResourceBookingList


router = routers.DefaultRouter()
router.register(r'resource', views.ResourceViewSet)
router.register(r'resourcesharing', views.ResourceSharingViewSet)
router.register(r'resourcebooking', views.ResourceBookingViewSet)
router.register(r'resource', views.ResourceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'resourcesharing'
urlpatterns = [
    path('api/', include(router.urls)),
    path('create/resource', CreateResourceView.as_view(), name="create_resource"),
    path('<int:pk>/edit/resource', EditResourceView.as_view(), name="edit_resource"),
    path('resource', ResourceList.as_view(), name='resource_list'),
    path('resourcesharing', ResourceSharingList.as_view(), name='resourcesharing_list'),
    path('resourcebooking', ResourceBookingList.as_view(), name='resourcebooking_list'),

]