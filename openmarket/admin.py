from django.contrib import admin
from django_cascading_dropdown_widget.widgets import DjangoCascadingDropdownWidget
from django_cascading_dropdown_widget.widgets import CascadingModelchoices
from .models import Seller, Product, ServiceProvider
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

