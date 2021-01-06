from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [

path('', views.landlordindex, name='lindex'),
path('home/', views.landlordhome, name='lhome'),
path('register/', views.landlordregister, name='lregister'),
path('profile/', views.landlordviewprofile, name='lprofile'),
path('profile/<int:id>/update/', views.landlordupdateProfile, name='lprofileupdate'),
path('login/', views.landlordloginpage, name='llogin'),
path('add/', views.addhouse, name='add-house'),
path('listing/', views.houselisting, name='house-listing'),
path('messages/', views.messages, name='messages'),
path('logout/', views.landlorduserlogout, name='llogout'),
path('resset/', auth_views.PasswordResetView.as_view(), name='reset-password'),

]