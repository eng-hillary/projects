from django.contrib import admin
from .models import Seller, Product, ServiceProvider,Service
from common.models import Region, District
from django import forms
#from .forms import ServiceProviderProfileForm
# Register your models here.


class SellerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
]
    search_fields = ['seller_type', 'business_location']

admin.site.register(Seller, SellerAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = [
       'name', 
       'enterprise', 
       'slug', 
       'image', 
       'description', 
       'price', 
       'available',
       'date_created', 
       'date_updated'
        
]
    search_fields = ['name', 'slug']

admin.site.register(Product, ProductAdmin)

class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = [
       'user'
]
    search_fields = ['user']

admin.site.register(ServiceProvider, ServiceProviderAdmin)

admin.site.register(Service)

