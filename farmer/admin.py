from django.contrib import admin
from .models import FarmerProfile,Group

# Register your models here.


class FarmerProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        

    ]
    search_fields = ['first_name']


admin.site.register(FarmerProfile, FarmerProfileAdmin)