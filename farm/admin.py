from django.contrib import admin
from .models import Sector, Enterprise
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
        'sector',
        'description'
        

    ]
    search_fields = ['name','sector','description']


admin.site.register(Enterprise, EnterpriseAdmin)