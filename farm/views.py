from django.shortcuts import render
from .models import Sector
from .serializers import SectorSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

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