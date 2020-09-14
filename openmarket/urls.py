from django.urls import include, path
from rest_framework import routers
from . import views
from .views import ProductList, SellerList, BuyerList


router = routers.DefaultRouter()
router.register(r'openmarket', views.ProductViewSet)
router.register(r'openmarket', views.SellerViewSet)
router.register(r'openmarket', views.BuyerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'openmarket'
urlpatterns = [
    path('', include(router.urls)),
    path('products', ProductList.as_view(), name='product_list'),
    path('sellers', SellerList.as_view(), name='seller_list'),
    path('sellers', BuyerList.as_view(), name='buyer_list'),
]