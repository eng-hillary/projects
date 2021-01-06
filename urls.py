from django.urls import path
from apis.views import ( api_house_detail_view, api_house_detail_update)

app_name = 'landlord'

urlpatterns = [
    path('house/<int:id>/', api_house_detail_view, name="house-api"),
    path('house/update/<int:id>', api_house_detail_view, name="house-api")
    ,]
