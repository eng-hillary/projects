from django.contrib import admin
from .models import Sector, Enterprise,Farm
# Register your models here.

class SectorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'size'
        

    ]
    search_fields = ['name','size']


admin.site.register(Sector, SectorAdmin)

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'farm',
        'description'
        

    ]
    search_fields = ['name','sector','description']


admin.site.register(Enterprise, EnterpriseAdmin)

class FarmAdmin(admin.ModelAdmin):
    list_display = [
        'farm_name',
        'farmer',
        'start_date',
        'close_date',
        'status',
        'lat',
        'lon',
        'availability_of_services',
        'availability_of_water',
        'land_occupied'
        

    ]
    search_fields = ['farm_name','status','lat','lon']


admin.site.register(Farm, FarmAdmin)