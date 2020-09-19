from django.contrib.auth import views as auth_views
from common.views import (
    HomePage, account_activation_sent, activate, SignUpView, ProfileView,
    PasswordResetView

)

from django.urls import path


app_name ='common'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgot-password/', PasswordResetView.as_view(), name='forgot_password'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
   
   


] 
