from django.shortcuts import render
from .models import Sector, Enterprise
from .serializers import SectorSerializer, EnterpriseSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
# views for sector
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

# views for enterprise
class EnterpriseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = Enterprise.objects.all().order_by('-id')
    serializer_class = EnterpriseSerializer
    permission_classes = [permissions.IsAuthenticated]


class EnterpriseList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'enterprise_list.html'

    def get(self, request):
        queryset = Enterprise.objects.order_by('-id')
        return Response({'enterprise': queryset})
