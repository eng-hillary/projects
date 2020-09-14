from django.shortcuts import render
from .models import FarmerProfile
from .serializers import GroupSerializer, FarmerProfileSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class FarmerListView():

<<<<<<< HEAD
    template_name = 'farmers_list.html'
=======
class GroupList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'group_list.html'

    def get(self, request):
        queryset = Group.objects.order_by('-id')
        return Response({'groups': queryset})


# views for farmerprofile
class FarmerProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = FarmerProfile.objects.all().order_by('region')
    serializer_class = FarmerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class FarmerProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'farmerprofile_list.html'

    def get(self, request):
        queryset = FarmerProfile.objects.order_by('region')
        return Response({'farmerprofiles': queryset})
>>>>>>> 8cdc5aa42aaf1cb2d5b5ecefe529b37f7e9fadac
