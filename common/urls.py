from django.contrib.auth import views as auth_views
from common.views import (
    HomePage,

)

from django.urls import path

app_name ='common'

urlpatterns = [
     path('', HomePage.as_view(), name='home'),

]
