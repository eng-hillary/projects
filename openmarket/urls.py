from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ProductList


router = routers.DefaultRouter()
router.register(r'openmarket', views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'openmarket'
urlpatterns = [
    path('', include(router.urls)),
    path('products', ProductList.as_view(), name='product_list'),
]