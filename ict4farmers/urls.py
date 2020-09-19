"""ict4farmers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from common .views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('common.urls', namespace="common")),
    
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('api-openmarket/', include('openmarket.urls', namespace="api-openmarket")),
    path('openmarket/', include('openmarket.urls', namespace="openmarket")),

    path('api-farm/', include('farm.urls', namespace="api-farm")),
    path('farm/', include('farm.urls', namespace="farm")),

    path('api-farmer/', include('farmer.urls', namespace="api-farmer")),
    path('farmer/', include('farmer.urls', namespace="farmer")),

    path('api-unffeagents/', include('unffeagents.urls', namespace="api-unffeagents")),
    path('unffeagents/', include('unffeagents.urls', namespace="unffeagents")),

    path('api-weather/', include('weather.urls', namespace="api-weather")),
    path('weather/', include('weather.urls', namespace="weather")),

    path('api-resourcesharing/', include('resourcesharing.urls', namespace="api-resourcesharing")),
    path('resourcesharing/', include('resourcesharing.urls', namespace="resourcesharing")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)