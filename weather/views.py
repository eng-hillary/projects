from django.shortcuts import render
from .models import CommunityWeather
from .serializers import CommunityWeatherSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

#views for products
class CommunityWeatherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = CommunityWeather.objects.all().order_by('weather')
    serializer_class = CommunityWeatherSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommunityWeatherList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'communityweather_list.html'

    def get(self, request):
        queryset = CommunityWeather.objects.order_by('weather')
        return Response({'communityweathers': queryset})
