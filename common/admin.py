from django.contrib import admin
from .models import Region, District, County, SubCounty, Parish, Village

class RegionAdmin(admin.ModelAdmin):
    list_display = [
        'name'
        
   ]
    search_fields = ['name']
admin.site.register(Region, RegionAdmin)


class DistrictAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'region'
        
   ]
    search_fields = ['name', 'region']
admin.site.register(District, DistrictAdmin)


class CountyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'district'
        
   ]
    search_fields = ['name', 'district']
admin.site.register(County, CountyAdmin)


class SubCountyAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'county'
        
   ]
    search_fields = ['name', 'county']
admin.site.register(SubCounty, SubCountyAdmin)



class ParishAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'sub_county'
        
   ]
    search_fields = ['name', 'sub_county']
admin.site.register(Parish, ParishAdmin)


class VillageAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'parish'
        
   ]
    search_fields = ['name', 'parish']
admin.site.register(Village, VillageAdmin)