from django.urls import include, path
from rest_framework import routers
from . import views
from .views import (AgentProfileList, MarketList, MarketPriceList, 
NoticeList,AgentProfileDetail,CreateAgentProfile)


router = routers.DefaultRouter()
router.register(r'agentprofile', views.AgentProfileViewSet)
router.register(r'market', views.MarketViewSet)
router.register(r'marketprice', views.MarketPriceViewSet)
router.register(r'notice', views.NoticeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

app_name = 'unffeagents'

urlpatterns = [
    path('', include(router.urls)),
    path('agentprofile', AgentProfileList.as_view(), name='agentprofile_list'),
    path('<int:pk>/edit/agentprofile', AgentProfileDetail.as_view(), name="edit_agentprofile"),
    path('create/agentprofile', CreateAgentProfile.as_view(), name="create_agentprofile"),

    path('market', MarketList.as_view(), name='market_list'),
    path('marketprice', MarketPriceList.as_view(), name='marketprice_list'),
    path('notice', NoticeList.as_view(), name='notice_list'),

]