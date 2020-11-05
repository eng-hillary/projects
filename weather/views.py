from django.shortcuts import render
from .models import CommunityWeather
from .serializers import CommunityWeatherSerializer, PostWeatherSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters

#views for products
class CommunityWeatherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    serializer_class = CommunityWeatherSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['id','weather','reported_by__first_name','date_reported','time_reported','description','lon','lat']
    ordering_fields = '__all__'

    def get_queryset(self):
       
        queryset =  CommunityWeather.objects.all().order_by('-id')
        lon = self.request.query_params.get('lon', None)
        if lon is not None:
            queryset = queryset.filter(lon=lon)
        lat = self.request.query_params.get('lat', None)
        if lon is not None:
            queryset = queryset.filter(lat=lat)
        return queryset

    def create(self, request, format=None):
        serializer = PostWeatherSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.status ='active'
                user = self.request.user
                serializer.save(reported_by = user)
            except:
                return Response({'error':'Failed to save'})
                
            return Response({'status':'successful'})
        return Response(serializer.errors, status=400)


class CommunityWeatherList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'communityweather_list.html'

    def get(self, request):
        queryset = CommunityWeather.objects.order_by('weather')
        return Response({'communityweathers': queryset})
