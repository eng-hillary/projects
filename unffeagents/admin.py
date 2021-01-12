from django.contrib import admin
from .models import Notice, AgentProfile, Market,MarketPrice

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

class AgentAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'contact',
            'region',
        'district',
        'specific_role'

    ]
    search_fields = ['user','specific_role','contact','district','region']


admin.site.register(AgentProfile, AgentAdmin)

class MarketAdmin(admin.ModelAdmin):
    list_display = [
        'market_name',
        'market_description',
        'location',
    

    ]
    search_fields = ['market_name','market_description','location']


admin.site.register(Market, MarketAdmin)

class MarketPriceAdmin(admin.ModelAdmin):
    list_display = [
        'market',
        'user',
        'product',
        'unit_of_measure',
        'max_price',
        'min_price',
        'created'
    

    ]
    search_fields = ['market__market_name','product__name','max_price','min_price','date_posted']


admin.site.register(MarketPrice, MarketPriceAdmin)
