from django.contrib.auth import views as auth_views
from common.views import (
    HomePage, account_activation_sent, activate, signup, UpdateProfileView, ProfileView

)

from django.urls import path

app_name ='common'

urlpatterns = [
     path('', HomePage.as_view(), name='home'),
     path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
     path('signup/', signup, name='signup'),
     path('activate/<uidb64>/<token>/', activate, name='activate'),

]
