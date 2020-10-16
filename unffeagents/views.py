from django.shortcuts import render
from .models import (AgentProfile, Market, MarketPrice, Notice,CallRsponse,Caller)
from .serializers import (AgentProfileSerializer, MarketSerializer, MarketPriceSerializer, 
NoticeSerializer,CallSerializer,ResponseSerializer)
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from .forms import (AgentProfileForm)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)

from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
from rest_framework import filters


# views for agentprofiles
class AgentProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agentprofiles to be viewed or edited.
    """
    queryset = AgentProfile.objects.all().order_by('specific_role')
    serializer_class = AgentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgentProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'agentprofile_list.html'

    def get(self, request):
        queryset = AgentProfile.objects.order_by('specific_role')
        return Response({'agentprofiles': queryset})


class CreateAgentProfile(LoginRequiredMixin,CreateView):
    template_name = 'create_agentprofile.html'
    success_url = reverse_lazy('unffeagents:agentprofile_list')
    form_class = AgentProfileForm
    success_message = "Your profile was created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateAgentProfile, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateAgentProfile, self).get_form_kwargs()
        return kwargs


    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
        return self.form_invalid(form)


    def form_valid(self, form):
        profile = form.save(commit=False)
        # setting farmer profile to in-active
        profile.user = self.request.user
        profile.save()

        # send email to farmer after registration
        current_site = get_current_site(self.request)
        subject = 'Registrated Successful'
        message = render_to_string('profile_created_successful.html', {
            'user': profile.user,
            'domain': current_site.domain
            })
        to_email = profile.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.send()
        return redirect('unffeagents:agentprofile_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))
# views for market
class MarketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows markets to be viewed or edited.
    """
    queryset = Market.objects.all().order_by('market_name')
    serializer_class = MarketSerializer
    permission_classes = [permissions.IsAuthenticated]


class MarketList(APIView):
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
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'notice_list.html'

    def get(self, request):
        queryset = Notice.objects.order_by('notice_title')
        return Response({'notices': queryset})


class CallerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = Caller.objects.all()
    serializer_class = CallSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class ResponseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = CallRsponse.objects.all()
    serializer_class = ResponseSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['session_id','duration','recording','agent__user__first_name','agent__user__last_name']
    ordering_fields = '__all__'
