from django.contrib import admin
from .models import (Sector, Enterprise,Farm,EnterpriseType, Query,RecordType,
 FarmRecord)
# Register your models here.

class SectorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'size'
        

    ]
    search_fields = ['name','size']


admin.site.register(Sector, SectorAdmin)

class QueryAdmin(admin.ModelAdmin):
    list_display = [
        'query_category',
        'farm',
        'description',
        'date_discovered',
        'action_taken',
        'image',
        'reporting_date',
        'solution'
        

    ]
    search_fields = ['name','size']


admin.site.register(Query, QueryAdmin)

class EnterpriseAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'farm',
        'description'
        

    ]
    search_fields = ['name','sector','description']


admin.site.register(Enterprise, EnterpriseAdmin)

class EnterpriseTypeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'sector',
        

    ]
    search_fields = ['name','sector__name']


admin.site.register(EnterpriseType, EnterpriseTypeAdmin)

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
admin.site.register(RecordType)
class FarmRecordAdmin(admin.ModelAdmin):
    list_display = [
        'enterprise',
        'record_type',
        'name',
        'from_date',
        'to_date',
        'taken_by',
        

    ]
    search_fields = ['enterprise__name','record_type__name','name','taken_by']
admin.site.register(FarmRecord, FarmRecordAdmin)