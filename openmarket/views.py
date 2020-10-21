from django.shortcuts import render
from .models import Product, Seller, Buyer, SellerPost, BuyerPost, ServiceProvider, Service, ContactDetails, Logistics,SoilScience
from common.models import Region, District
from .serializers import (ProductSerializer,
                        SellerSerializer, 
                        BuyerSerializer, 
                        SellerPostSerializer,
                        BuyerPostSerializer,
                        ServiceProviderSerializer, 
                        ServiceRegistrationSerializer,
                        ContactDetailsSerializer,
                        LogisticsSerializer,
                        SoilScienceSerializer,
                        ServiceProviderApprovalSerializer,
                        SellerApprovalSerializer,
                        PostServiceProviderSerializer,
                        PostServiceRegistrationSerializer
                        )
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import(SellerProfileForm,ProductProfileForm, ServiceProviderProfileForm, ServiceProfileForm)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)

from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
import datetime
from django.db import IntegrityError

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductList(APIView):
    permission_classes = (IsAuthenticated,) 
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'product_list.html'

    def get(self, request):
        queryset = Product.objects.order_by('-id')
        return Response({'products': queryset})


'''
Create Product profile. Used class based view.
'''
class CreateProductProfile(CreateView):
    template_name = 'create_product_profile.html'
    success_url = reverse_lazy('openmarket:profile_list')
    form_class = ProductProfileForm
    success_message = "Product profile was created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateProductProfile, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateProductProfile, self).get_form_kwargs()
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
        # setting product profile to pending
        profile.status = 'pending'
        profile.user = self.request.user
        profile.save()
        return redirect('openmarket:product_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))
        
#views for sellers
class SellerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Seller.objects.all().order_by('seller_type')
    serializer_class = SellerSerializer
    #permission_classes = [permissions.IsAuthenticated]


    def approved(self, request, pk, format=None):
        profile = self.get_object()
        serializer = SellerApprovalSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(status ='Active', approved_date = datetime.datetime.now(),approver=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def decline(self, request, pk, format=None):
        profile = self.get_object()
        serializer = SellerApprovalSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(status ='Rejected', approved_date = datetime.datetime.now(),approver=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class SellerList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'seller_list.html'

    def get(self, request):
        queryset = Seller.objects.order_by('seller_type')
        return Response({'sellers': queryset})

'''
Create Seller profile. Used class based view.
'''
class CreateSellerProfile(LoginRequiredMixin,CreateView):
    template_name = 'create_seller_profile.html'
    success_url = reverse_lazy('openmarket:seller_list')
    form_class = SellerProfileForm
    success_message = "Your profile was created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateSellerProfile, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateSellerProfile, self).get_form_kwargs()
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
        profile.status = 'pending'
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
        return redirect('openmarket:seller_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))
#views for buyers
class BuyerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Buyer.objects.all().order_by('created')
    serializer_class = BuyerSerializer
    permission_classes = [permissions.IsAuthenticated]


class BuyerList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'buyer_list.html'

    def get(self, request):
        queryset = Buyer.objects.order_by('created')
        return Response({'buyers': queryset})


#views for sellerpost
class SellerPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = SellerPost.objects.all().order_by('-name')
    serializer_class = SellerPostSerializer
    permission_classes = [permissions.IsAuthenticated]


class SellerPostList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sellerpost_list.html'

    def get(self, request):
        queryset = SellerPost.objects.order_by('-name')
        return Response({'sellerposts': queryset})


#views for buyerpost
class BuyerPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = BuyerPost.objects.all().order_by('name')
    serializer_class = BuyerPostSerializer
    permission_classes = [permissions.IsAuthenticated]


class BuyerPostList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'buyerpost_list.html'

    def get(self, request):
        queryset = BuyerPost.objects.order_by('name')
        return Response({'buyerposts': queryset})


#views for service provider
class ServiceProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = ServiceProvider.objects.all().order_by('service_type')
    serializer_class = ServiceProviderSerializer
    permission_classes = [permissions.IsAuthenticated]


    def approved(self, request, pk, format=None):
        profile = self.get_object()
        serializer = ServiceProviderApprovalSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(status ='Active', approved_date = datetime.datetime.now(),approver=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def decline(self, request, pk, format=None):
        profile = self.get_object()
        serializer = ServiceProviderApprovalSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(status ='Rejected', approved_date = datetime.datetime.now(),approver=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def create(self, request, format=None):
        serializer = PostServiceProviderSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.status ='Pending'
                #serializer.user = self.request.user
                serializer.save(user = self.request.user)
            except IntegrityError:
                return Response({'error':'Service Provider account already exists'})
                
            return Response({'status':'successful'})
        return Response(serializer.errors, status=400)


class ServiceProviderList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'serviceprovider_list.html'

    def get(self, request):
        queryset = ServiceProvider.objects.order_by('service_type')
        return Response({'serviceproviders': queryset})

#View for creating a service
class CreateServiceView(LoginRequiredMixin,CreateView):
    template_name = 'register_service.html'
    success_url = reverse_lazy('openmarket:serviceregistration_list')
    form_class = ServiceProfileForm
    success_message = "Your profile was created successfully"
    

    def dispatch(self, request, *args, **kwargs):
        return super(CreateServiceView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateServiceView, self).get_form_kwargs()
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
        subject = 'Registrated Service Successful'
        message = render_to_string('profile_created_successful.html', {
            'user': profile.user,
            'domain': current_site.domain
            })
        to_email = profile.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
        email.send()
        return redirect('openmarket:serviceregistration_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


#views for service registration 

class ServiceRegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Service.objects.all().order_by('service_name')
    serializer_class = ServiceRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, format=None):
        serializer = PostServiceRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            try:
            #     serializer.status ='Pending'
                #serializer.user = self.request.user
                serializer.save(user = self.request.user)
            except IntegrityError:
                return Response({'error':'Service account already exists'})
                
            return Response({'status':'successful'})
        return Response(serializer.errors, status=400)

class MapServiceDetailView(DetailView):
    model = Service
    template_name = "map_service_detail.html"

    def get_context_data(self, **kwargs):
        context = super(MapServiceDetailView, self).get_context_data(**kwargs)
        context['Serviceobject'] = self.object
        
        return context


#service provider list
class ServiceProviderProfileList(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'serviceprovider_list.html'

    def get(self, request):
        queryset = ServiceProvider.objects.order_by('region')
        return Response({'serviceproviders': queryset})

 
#views for creating a service provider profile

class CreateServiceProviderProfile(LoginRequiredMixin,CreateView):
    template_name = 'register_service_provider.html'
    success_url = reverse_lazy('openmarket:serviceprovider_list')
    form_class = ServiceProviderProfileForm
    success_message = "Your profile was created successfully"
    

    def dispatch(self, request, *args, **kwargs):
        return super(CreateServiceProviderProfile, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateServiceProviderProfile, self).get_form_kwargs()
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
        subject = 'Registrated Successful'
        message = render_to_string('service_provider_reg_email.html', {
            'user': profile.user,
            'domain': current_site.domain
            })
        to_email = profile.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
        email.send()
        return redirect('openmarket:serviceprovider_list')

#view for loading 
def load_districts(request):
    region_id = request.GET.get('region')
    districts = District.objects.filter(region_id=region_id).order_by('name')
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})




class ServiceRegistrationList(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'serviceregistration_list.html'

    def get(self, request):
        return Response()


#views for ContactDetails
class ContactDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = ContactDetails.objects.all().order_by('name')
    serializer_class = ContactDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactDetailsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contactdetails_list.html'

    def get(self, request):
        queryset = ContactDetails.objects.order_by('name')
        return Response({'contactdetails': queryset})


#views for Logistics
class LogisticsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Logistics.objects.all().order_by('name')
    serializer_class = LogisticsSerializer
    permission_classes = [permissions.IsAuthenticated]


class LogiticsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'logistics_list.html'

    def get(self, request):
        queryset = Logistics.objects.order_by('name')
        return Response({'logistics': queryset})



#views for packaging
class SoilScienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = SoilScience.objects.all().order_by('name')
    serializer_class = SoilScienceSerializer
    permission_classes = [permissions.IsAuthenticated]


class SoilScienceList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'soilscience_list.html'

    def get(self, request):
        queryset = SoilScience.objects.order_by('name')
        return Response({'soilsciences': queryset})
    

#update service provider view
class UpdateServiceProviderProfile(LoginRequiredMixin,UpdateView):
    model =ServiceProvider
    template_name = 'register_service_provider.html'
    success_url = reverse_lazy('openmarket:serviceprovider_list')
    form_class = ServiceProviderProfileForm
    success_message = "Your profile was Updated successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(UpdateServiceProviderProfile, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(UpdateServiceProviderProfile, self).get_form_kwargs()
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

        return redirect('farmer:farmerprofile_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


#Service Provider Detail View
class ServiceProviderProfileDetailView(LoginRequiredMixin, DetailView):
    model = ServiceProvider
    context_object_name = "providerrecord"
    template_name = "view_service_provider_profile.html"

    def get_context_data(self, **kwargs):
        context = super(ServiceProviderProfileDetailView, self).get_context_data(**kwargs)
        
        context.update({

        })
        return context


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Service
    context_object_name = "profilerecord"
    template_name = "view_services_details.html"

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        
        context.update({

        })
        return context

