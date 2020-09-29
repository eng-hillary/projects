from django.contrib.auth import views as auth_views
from common.views import (
    HomePage, account_activation_sent, activate, SignUpView, ProfileView,
    ForgotPasswordView, load_districts, load_counties,load_sub_counties,
    load_parishes,load_villages
)

from django.urls import path


app_name ='common'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # load districts url
    path('ajax/load-districts/', load_districts, name='ajax_load_districts'),
    path('ajax/load-counties/', load_counties, name='ajax_load_counties'),
    path('ajax/load-sub_counties/', load_sub_counties, name='ajax_load_sub_counties'),
    path('ajax/load-parishes/', load_parishes, name='ajax_load_parishes'),
    path('ajax/load-villages/', load_villages, name='ajax_load_villages'),

   
] 
