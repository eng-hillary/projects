from django.shortcuts import render
from .models import AgentProfile, Market, MarketPrice, Notice
from .serializers import AgentProfileSerializer, MarketSerializer, MarketPriceSerializer, NoticeSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# views for agentprofiles
class AgentProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agentprofiles to be viewed or edited.
    """
    queryset = AgentProfile.objects.all().order_by('specific_role')
    serializer_class = AgentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgentProfileList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'agentprofile_list.html'

    def get(self, request):
        queryset = AgentProfile.objects.order_by('specific_role')
        return Response({'agentprofiles': queryset})


class AgentProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'agentprofile_detail.html'

    def get(self, request, pk):
        agentprofile = get_object_or_404(AgentProfile, pk=pk)
        serializer = AgentProfileSerializer(agentprofile)
        return Response({'serializer': serializer, 'agentprofile': agentprofile})

    def post(self, request, pk):
        agentprofile = get_object_or_404(AgentProfile, pk=pk)
        serializer = AgentProfileSerializer(agentprofile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'agentprofile': agentprofile})
        serializer.save()
        return redirect('unffeagents:agentprofile_list')

class CreateAgentProfile(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create_agentprofile.html'

    def get(self, request):
        agentprofile = None
        serializer = AgentProfileSerializer()
        return Response({'serializer': serializer, 'agentprofile': agentprofile})

    def post(self, request):
        serializer = AgentProfileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('unffeagents:agentprofile_list')

# views for market
class MarketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows markets to be viewed or edited.
    """
    queryset = Market.objects.all().order_by('market_name')
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]


class MarketList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'market_list.html'

    def get(self, request):
        queryset = Market.objects.order_by('market_name')
        return Response({'markets': queryset})
        

# views for marketprice
class MarketPriceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows marketprices to be viewed or edited.
    """
    queryset = MarketPrice.objects.all().order_by('market')
    serializer_class = MarketPriceSerializer
    permission_classes = [permissions.IsAuthenticated]


class MarketPriceList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'marketprice_list.html'

    def get(self, request):
        queryset = MarketPrice.objects.order_by('market')
        return Response({'marketprices': queryset})


# views for notices
class NoticeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notices to be viewed or edited.
    """
    queryset = Notice.objects.all().order_by('notice_title')
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAuthenticated]


class NoticeList(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'notice_list.html'

    def get(self, request):
        queryset = Notice.objects.order_by('notice_title')
        return Response({'notices': queryset})