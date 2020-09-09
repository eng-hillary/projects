from django.shortcuts import render
from .models import Sector
from .serializers import SectorSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

# Create your views here.
class SectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = Sector.objects.all().order_by('-id')
    serializer_class = SectorSerializer
    permission_classes = [permissions.IsAuthenticated]


class SectorList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sector_list.html'

    def get(self, request):
        queryset = Sector.objects.order_by('-id')
        return Response({'sectors': queryset})


class SectorDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sector_detail.html'

    def get(self, request, pk):
        sector = get_object_or_404(Sector, pk=pk)
        serializer = SectorSerializer(sector)
        return Response({'serializer': serializer, 'sector': sector})

    def post(self, request, pk):
        sector = get_object_or_404(Sector, pk=pk)
        serializer = SectorSerializer(sector, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'sector': sector})
        serializer.save()
        return redirect('farms:sector_list')


class CreateSector(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create_sector.html'

    def get(self, request):
        sector = None
        serializer = SectorSerializer()
        return Response({'serializer': serializer, 'sector': sector})

    def post(self, request):
        serializer = SectorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('farms:sector_list')