from django.contrib import admin
from .models import Notice

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = [
        'notice_title',
        'created',
        'display_up_to',
        'posted_by',

        

    ]
    search_fields = ['notice_title','created']


admin.site.register(Notice, NoticeAdmin)
