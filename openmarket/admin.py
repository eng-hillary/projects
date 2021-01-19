from django.contrib import admin
from .models import Seller,ProductCategory, Product, ServiceProvider,Service,Category,SellerPost
from common.models import Region, District
from django import forms
#from .forms import ServiceProviderProfileForm
# Register your models here.


class SellerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
]
    search_fields = ['seller_type', 'location']

admin.site.register(Seller, SellerAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug'
    ]

    search_fields = ['name', 'slug']

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
       'name', 
       'slug',
       'local_name', 
       'image', 
       'description', 
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

class ServiceAdmin(admin.ModelAdmin):
    list_display = [
       'service_name',  
       'location',  
       'availability_date', 
       'picture', 
        
]
admin.site.register(Service,  ServiceAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
       'cat_name'
       
]
admin.site.register(Category, CategoryAdmin)


class SellerPostAdmin(admin.ModelAdmin):
    list_display = [
       'seller', 
       'product', 
       'quantity', 
       'price_offer', 
       'delivery_option', 
       'payment_options', 
       'payment_mode',
       'product_description'
        
]
    search_fields = ['seller', 'product_description','payment_mode','payment_mode']

admin.site.register(SellerPost, SellerPostAdmin)