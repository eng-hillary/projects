from django.shortcuts import render
from .models import Resource, ResourceSharing, ResourceBooking
from .serializers import ResourceSerializer, ResourceSharingSerializer, ResourceBookingSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# views for resources
class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agentprofiles to be viewed or edited.
    """
    queryset = Resource.objects.all().order_by('resource_name')
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResourceList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'resource_list.html'

    def get(self, request):
        queryset = Resource.objects.order_by('resource_name')
        return Response({'resources': queryset})



# views for resource sharing
class ResourceSharingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agentprofiles to be viewed or edited.
    """
    queryset = ResourceSharing.objects.all().order_by('resource')
    serializer_class = ResourceSharingSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResourceSharingList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'resourcesharing_list.html'

    def get(self, request):
        queryset = ResourceSharing.objects.order_by('resource')
        return Response({'resourcesharings': queryset})



# views for resource booking
class ResourceBookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agentprofiles to be viewed or edited.
    """
    queryset = ResourceBooking.objects.all().order_by('resource')
    serializer_class = ResourceBookingSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResourceBookingList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'resourcebooking_list.html'

    def get(self, request):
        queryset = ResourceBooking.objects.order_by('resource')
        return Response({'resourcebookings': queryset})

