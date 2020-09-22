from django.shortcuts import render
from .models import Product, Seller, Buyer, SellerPost, BuyerPost, ServiceProvider, ServiceRegistration, ContactDetails, Logistics, Storage, Packaging, Medical, SoilScience
from .serializers import (ProductSerializer,
                        SellerSerializer, 
                        BuyerSerializer, 
                        SellerPostSerializer,
                        BuyerPostSerializer,
                        ServiceProviderSerializer, 
                        ServiceRegistrationSerializer,
                        ContactDetailsSerializer,
                        LogisticsSerializer,
                        StorageSerializer,
                        MedicalSerializer,
                        PackagingSerializer,
                        SoilScienceSerializer)
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import(SellerProfileForm,ProductProfileForm)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)

from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
    
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductList(APIView):
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
        # setting product profile to in-active
        profile.status = 'in_active'
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


class ServiceProviderList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'serviceprovider_list.html'

    def get(self, request):
        queryset = ServiceProvider.objects.order_by('service_type')
        return Response({'serviceproviders': queryset})


#views for service registration
class ServiceRegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = ServiceRegistration.objects.all().order_by('service_id')
    serializer_class = ServiceRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceRegistrationList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'serviceregistration_list.html'

    def get(self, request):
        queryset = ServiceRegistration.objects.order_by('service_id')
        return Response({'serviceregistrations': queryset})


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


#views for StoragePackagingSerializerViewSet
class StorageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Storage.objects.all().order_by('name')
    serializer_class = StorageSerializer
    permission_classes = [permissions.IsAuthenticated]


class StorageList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'storage_list.html'

    def get(self, request):
        queryset = Storage.objects.order_by('name')
        return Response({'storages': queryset})


#views for packaging
class PackagingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Packaging.objects.all().order_by('name')
    serializer_class = PackagingSerializer
    permission_classes = [permissions.IsAuthenticated]


class PackagingList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'packaging_list.html'

    def get(self, request):
        queryset = Packaging.objects.order_by('name')
        return Response({'packagings': queryset})


#views for packaging
class MedicalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Packaging.objects.all().order_by('name')
    serializer_class = MedicalSerializer
    permission_classes = [permissions.IsAuthenticated]


class MedicalList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'medical_list.html'

    def get(self, request):
        queryset = Medical.objects.order_by('name')
        return Response({'medicals': queryset})


#views for packaging
class SoilScienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Packaging.objects.all().order_by('name')
    serializer_class = SoilScienceSerializer
    permission_classes = [permissions.IsAuthenticated]


class SoilScienceList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'soilscience_list.html'

    def get(self, request):
        queryset = SoilScience.objects.order_by('name')
        return Response({'soilsciences': queryset})