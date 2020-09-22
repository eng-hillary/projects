from django.contrib import admin
from .models import Seller, Product
# Register your models here.


class SellerAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'business_number',
        'business_location', 
        'seller_type', 
        'date_of_birth',
        'region',
        'district', 
        'county', 
        'sub_county', 
        'parish', 
        'village', 
        'gender',
        'marital_status', 
        'enterprise',
        'major_products', 
        'status', 
        'approver',
        'approved_date',
        
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
