from django.urls import include, path
from rest_framework import routers
from . import views

from .views import (ProductList,
                    SellerList,
                    CreateSellerProfile,
                    CreateProductProfile,
                    BuyerList,
                    ServiceProviderList,
                    ServiceRegistrationList,
                    SellerPostList,
                    BuyerPostList,
                    ContactDetailsList,
                    LogiticsList,
                    StorageList,
                    PackagingList,
                    MedicalList,
                    SoilScienceList)


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'sellers', views.SellerViewSet)
router.register(r'buyers', views.BuyerViewSet)
router.register(r'sellerposts', views.SellerPostViewSet)
router.register(r'buyersposts', views.BuyerPostViewSet)
router.register(r'serviceproviders', views.ServiceProviderViewSet)
router.register(r'serviceregistration', views.ServiceRegistrationViewSet)
router.register(r'contactdetails', views.ContactDetailsViewSet)
router.register(r'logistics', views.LogisticsViewSet)
router.register(r'storages', views.StorageViewSet)
router.register(r'packagings', views.PackagingViewSet)
router.register(r'medicals', views.MedicalViewSet)
router.register(r'soilsciences', views.SoilScienceViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'openmarket'
urlpatterns = [
    path('', include(router.urls)),
    path('products', ProductList.as_view(), name='product_list'),
    path('create/products', CreateProductProfile.as_view(), name="create_product"),
    path('sellers', SellerList.as_view(), name='seller_list'),
    path('create/profile', CreateSellerProfile.as_view(), name="create_seller"),
    path('buyers', BuyerList.as_view(), name='buyer_list'),
    path('sellerposts', SellerPostList.as_view(), name='sellerpost_list'),
    path('buyerposts', BuyerPostList.as_view(), name='buyerpost_list'),
    path('serviceproviders', ServiceProviderList.as_view(), name='serviceprovider_list'),
    path('serviceregistration', ServiceRegistrationList.as_view(), name='serviceregistration_list'),
    path('contactdetails', ContactDetailsList.as_view(), name='contactdetails_list'),
    path('logistics', LogiticsList.as_view(), name='logistics_list'),
    path('storages', StorageList.as_view(), name='storage_list'),
    path('packagings', PackagingList.as_view(), name='packaging_list'),
    path('medicals', MedicalList.as_view(), name='medical_list'),
    path('soilsciences', SoilScienceList.as_view(), name='soilscience_list'),

]
