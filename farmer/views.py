from django.shortcuts import render
from .models import Group, FarmerProfile
from .serializers import GroupSerializer, FarmerProfileSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# views for groups
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
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
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'farmerprofile_list.html'

    def get(self, request):
        queryset = FarmerProfile.objects.order_by('region')
        return Response({'farmerprofiles': queryset})
