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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)
from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
from .forms import(FarmerProfileForm)

# views for groups
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class FarmerListView():

    template_name = 'farmers_list.html'

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


class FarmerProfileList(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'farmerprofile_list.html'

    def get(self, request):
        queryset = FarmerProfile.objects.order_by('region')
        return Response({'farmerprofiles': queryset})


'''
Create farmer profile. Used class based view.
'''
class CreateFarmerProfile(LoginRequiredMixin,CreateView):
    template_name = 'create_farmer_profile.html'
    success_url = reverse_lazy('farmer:farmerprofile_list')
    form_class = FarmerProfileForm
    success_message = "Your profile was created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateFarmerProfile, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateFarmerProfile, self).get_form_kwargs()
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
        profile.status = 'in_active'
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
        return redirect('farmer:farmerprofile_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))