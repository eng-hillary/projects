from django.urls import include, path
from rest_framework import routers
from . import views
from .views import (AgentProfileList, MarketList, MarketPriceList, 
NoticeList,CreateAgentProfile)


router = routers.DefaultRouter()
router.register(r'agentprofile', views.AgentProfileViewSet)
router.register(r'market', views.MarketViewSet)
router.register(r'marketprice', views.MarketPriceViewSet)
router.register(r'notice', views.NoticeViewSet)
router.register(r'call', views.CallerViewSet)
router.register(r'response', views.ResponseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'unffeagents'

urlpatterns = [
    path('api/', include(router.urls)),
    path('agentprofile', AgentProfileList.as_view(), name='agentprofile_list'),
    path('create/agentprofile', CreateAgentProfile.as_view(), name="create_agentprofile"),

    path('market', MarketList.as_view(), name='market_list'),
    path('marketprice', MarketPriceList.as_view(), name='marketprice_list'),
    path('notice', NoticeList.as_view(), name='notice_list'),

]