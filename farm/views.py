from django.shortcuts import render
from .models import Sector, Enterprise
from .serializers import SectorSerializer, EnterpriseSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

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