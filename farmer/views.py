from django.shortcuts import render
from .models import Group, FarmerProfile
from .serializers import GroupSerializer, FarmerProfileSerializer, FarmerApprovalSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from common.tokens import account_activation_token
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
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)
from .forms import(FarmerProfileForm,FarmerGroupForm)
import datetime
from django.db.models import Count, Q
import json


# views for groups
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupList(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'group_list.html'

    def get(self, request):
        queryset = Group.objects.order_by('-id')
        return Response({'groups': queryset})


# create farmer groups
class CreateFarmerGroup(LoginRequiredMixin,CreateView):
    template_name = 'create_farmer_group.html'
    success_url = reverse_lazy('farmer:group_list')
    form_class = FarmerGroupForm
    success_message = "Group has been created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateFarmerGroup, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateFarmerGroup, self).get_form_kwargs()
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
        group = form.save(commit=False)
        group.save()

        return redirect('farmer:group_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))

# edit farmer group

class EditFarmerGroup(LoginRequiredMixin,UpdateView):
    model =Group
    template_name = 'create_farmer_group.html'
    success_url = reverse_lazy('farmer:group_list')
    form_class = FarmerGroupForm
    success_message = "Group has been updated successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(EditFarmerGroup, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditFarmerGroup, self).get_form_kwargs()
        return kwargs


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
        return self.form_invalid(form)


    def form_valid(self, form):
        group = form.save(commit=False)
        group.save()

        return redirect('farmer:group_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))

# views for farmerprofile
class FarmerProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = FarmerProfile.objects.all().order_by('region')
    serializer_class = FarmerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def approved(self, request, pk, format=None):
        profile = self.get_object()
        serializer = FarmerApprovalSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(status ='Active', approved_date = datetime.datetime.now(),approver=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def decline(self, request, pk, format=None):
        profile = self.get_object()
        serializer = FarmerApprovalSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(status ='Rejected', approved_date = datetime.datetime.now(),approver=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



class FarmerProfileList(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'farmerprofile_list.html'

    def get(self, request):
        return Response()


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
        profile.status = 'Pending'
        profile.user = self.request.user
        profile.save()

        # send email to farmer after registration
        current_site = get_current_site(self.request)
        subject = 'Registered Successfully'
        message = render_to_string('profile_created_successful_email.html', {
            'user': profile.user,
            'domain': current_site.domain
            })
        to_email = profile.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
        email.send()
        return redirect('farmer:farmerprofile_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))

'''
Activate farmer profile
'''

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        group = Group.objects.get(name='Buyers')
        user.groups.add(group)
        user.save()
        login(request, user)
        return redirect('common:home')
    else:
        return render(request, 'account_activation_invalid.html')


'''
Edit farmer profile profile
'''
class UpdateFarmerProfile(LoginRequiredMixin,UpdateView):
    model =FarmerProfile
    template_name = 'create_farmer_profile.html'
    success_url = reverse_lazy('farmer:farmerprofile_list')
    form_class = FarmerProfileForm
    success_message = "Your profile was Updated successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(UpdateFarmerProfile, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(UpdateFarmerProfile, self).get_form_kwargs()
        return kwargs


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
        return self.form_invalid(form)


    def form_valid(self, form):
        profile = form.save(commit=False)
        # updating profile for only changed fields
        profile.save()

        # not sending email to a farmer after editing for now
        # current_site = get_current_site(self.request)
        # subject = 'Registrated Successful'
        # message = render_to_string('profile_created_successful_email.html', {
        #     'user': profile.user,
        #     'domain': current_site.domain
        #     })
        # to_email = profile.user.email
        # email = EmailMessage(
        #         subject, message, to=[to_email]
        #     )
        # email.content_subtype = "html"
        # email.send()
        return redirect('farmer:farmerprofile_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


#Quering the farmers table for the data. 
def farmer_class_view(request):
    #Filtering the needed columns for the bargraph
    dataset = FarmerProfile.objects \
        .values('region') \
        .annotate(credit_access_count=Count('region', filter=Q(credit_access=True)),
                  no_credit_access_count=Count('region', filter=Q(credit_access=False))) \
        .order_by('region')
#Creating lists 
    categories = list()
    credit_access_series_data = list()
    no_credit_access_series_data = list()

#Looping through the created dataset from above
    for entry in dataset:
        categories.append('%s Farmers' % entry['region'])
        credit_access_series_data.append(entry['credit_access_count'])
        no_credit_access_series_data.append(entry['no_credit_access_count'])


    credit_access_series = {
        'name': 'Credit Access',
        'data': credit_access_series_data,
        'color': 'green'
    }

    no_credit_access_series = {
        'name': 'No credit Access',
        'data': no_credit_access_series_data,
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Farmers Credit Access by Region'},
        'xAxis': {'categories': categories},
        'series': [credit_access_series, no_credit_access_series]
    }

    dump = json.dumps(chart)
    return render(request, 'credit.html', {'chart': dump})
    