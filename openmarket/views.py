from django.shortcuts import render,get_object_or_404
from .models import (Product, Seller, SellerPost, BuyerPost, 
ServiceProvider, Service, ContactDetails, Logistics, SoilScience, 
Category,SellerPost, ProductCategory)
from common.models import Region, District
from .serializers import (ProductSerializer,
                          SellerSerializer,
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
                          PostServiceRegistrationSerializer,
                          CategorySerializer,PostSellerSerializer,ProductCategorySerializer,PostSellerPostSerializer)
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import(SellerProfileForm, ProductProfileForm,ServiceProviderProfileForm, ServiceProfileForm,BuyerPostForm,SellerPostForm)

from .forms import(SellerProfileForm, ProductProfileForm,

                   ServiceProviderProfileForm, ServiceProfileForm,SellerPostForm)


from django.shortcuts import redirect
from django.contrib.auth.models import Group as UserGroup
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import (HttpResponseRedirect, JsonResponse, HttpResponse,
                         Http404)

from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
import datetime
from django.db import IntegrityError
from django.contrib.auth.models import Group
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from common.menu import has_group
from unffeagents.models import MarketPrice



class ProductViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        retrieve a sigle Product by its id

    list:
        Return a list of all Products.

    create:
        Create a new Product.E.g
        {
        "name": "Chicken",
        "slug": null,
        "image": "product_image_url", # product's image
        "description": "Chicken both hen and cock",
        "category": 7
    }

    destroy:
        Delete a Product.

    update:
        Update a Product.

    partial_update:
        Update a Product.
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]



class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer



class CategoryViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        retrieve a sigle category by its id

    list:
        Return a list of all Categories.

    create:
        Create a new Category.

    destroy:
        Delete a Category.

    update:
        Update a Category.

    partial_update:
        Update a Category.
    """
    queryset = Category.objects.order_by('-id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['id', 'cat_name']
    ordering_fields = '__all__'


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
       
        profile.seller = self.request.user
        profile.save()
        return redirect('openmarket:product_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


# update product view
class EditProductView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'create_product_profile.html'
    success_url = reverse_lazy('openmarket:product_list')
    form_class = ProductProfileForm
    success_message = "Product has been updated successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(EditProductView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditProductView, self).get_form_kwargs()
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
        farm = form.save(commit=False)
       
        farm.save()
        return redirect('openmarket:product_list')


# views for sellers


class SellerViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        retrieve a sigle Seller by its id

    list:
        Return a list of all Sellers.

    create:
        Create a new Seller.e.g
        {
        "business_number": "+256788329636",
        "seller_type": "wholeseller",
        "major_products": [7,6,5],
        "status": "Pending"
        "business_address":"Kampala"
    }

    destroy:
        Delete a Seller.

    update:
        Update a Seller.

    partial_update:
        Update a Seller.
    """
    queryset = Seller.objects.all().order_by('seller_type')
    serializer_class = SellerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """
        This view should return a list of all the sellers or 
        for the currently authenticated user.
        """
        user = self.request.user
        sellers = Seller.objects.order_by('-user')
        if  self.request.user.has_perm('openmarket.delete_seller') or self.request.user.is_superuser:
            queryset = sellers
        else:
            queryset = sellers.filter(user=user)
        
        return queryset


    def approved(self, request, pk, format=None):
        profile = self.get_object()
        serializer = SellerApprovalSerializer(profile, data=request.data)
        if serializer.is_valid():
            seller_group = Group.objects.get(name='Sellers')
            profile.user.groups.add(seller_group)
            serializer.save(status='Active', approved_date=datetime.datetime.now(
            ), approver=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def decline(self, request, pk, format=None):
        profile = self.get_object()
        serializer = SellerApprovalSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(status='Rejected', approved_date=datetime.datetime.now(
            ), approver=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def create(self, request, format=None):
        serializer = PostSellerSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save(user = self.request.user)
                serializer.save()
            except IntegrityError:
                return Response({'error':'Seller account already exists'})
                
            return Response({'status':'successful'})
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


class CreateSellerProfile(LoginRequiredMixin, CreateView):
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
        form.save_m2m()
      
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
        email.content_subtype = "html"
        email.send()
        return redirect('openmarket:seller_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form, major_products=self.major_products))
# views for buyers

#Get Context data
    def get_context_data(self, **kwargs):
        context = super(CreateSellerProfile, self).get_context_data(**kwargs)
        context["seller_form"] = context["form"]


        print("kwargs", self.kwargs)
        # context['call'] = Call.objects.get(pk=self.kwargs['call_pk']
        
        return context


# views for sellerpost
class SellerPostViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        retrieve a sigle Seller Post by its id

    list:
        Return a list of all Seller Posts.

    create:
        Create a new Seller Post.e.g
        {
        "product": "Milk",
        "market": 1,
        "quantity": 200.0,
        "price_offer": "1100.04",
        "delivery_option": "Pick up from the market",
        "payment_options": "credit", # options['credit','full_payment','installements','exchange']
        "payment_mode": "cash", # options['cash','bank','cheque','mobilemoney','credit_card','others']
        "product_description": "Water melon",
        "product_image_1": "http://127.0.0.1:8000/uploads/FB_IMG_15888191318596590.jpg",
        "product_image_2": "http://127.0.0.1:8000/uploads/FB_IMG_15878330260195603_SaIZmeP.jpg"
    }
      
    delete:
        Delete a Selller Post.

    PUT:
        Update a Seller Post.

    partial_update:
        Update a Seller Post.
    """
    #queryset = SellerPost.objects.all().order_by('-id')
    serializer_class = SellerPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def get_queryset(self):
        """
        This view should return a list of all the sellerposts
        for the currently authenticated user.
        """
        user = self.request.user
        products = SellerPost.objects.all().order_by('-id')
        if self.request.user.is_superuser or self.request.user.has_perm('openmarket.delete_sellerpost'):
            queryset = products
        else:
            seller = Seller.objects.get(user= user)
            queryset = products.filter(seller=seller)
        
        return queryset

    def create(self, request, format=None):
        serializer = PostSellerPostSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save(seller=self.request.user)
            except:
                return Response({'error': 'An error occured while posting your data'})

            return Response({'status': 'successful'})
        return Response(serializer.errors, status=400)


class SellerPostList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sellerpost_list.html'

    def get(self, request):
        queryset = SellerPost.objects.order_by('-name')
        return Response({'sellerposts': queryset})


# views for buyerpost
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
        queryset = BuyerPost.objects.order_by('-name')
        return Response({'buyerposts': queryset})


# views for service provider
class ServiceProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    #queryset = ServiceProvider.objects.all().order_by('nin')
    serializer_class = ServiceProviderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the service  provider profiles
        for the currently authenticated user.
        """
        user = self.request.user
        servicesproviders = ServiceProvider.objects.order_by('-user_id')
        if self.request.user.is_superuser or self.request.user.has_perm('openmarket.delete_serviceprovider'):
            queryset = servicesproviders
        else:
            queryset = servicesproviders.filter(user=user)

        return queryset

    def approved(self, request, pk, format=None):
        profile = self.get_object()
        serializer = ServiceProviderApprovalSerializer(
            profile, data=request.data)
        if serializer.is_valid():
            provider_group = UserGroup.objects.get(name='Service Providers')
            profile.user.groups.add(provider_group)
            serializer.save(status='Active', approved_date=datetime.datetime.now(),
                            approver=self.request.user)
            # sending message to the service provider for notification
            user = profile.user
            current_site = get_current_site(request)
            subject = 'Your application has been Approved'
            message = render_to_string('farm_created_successful_email.html', {
                'user': user,
                'domain': current_site.domain,
                'message': 'Your application as a service provider has been approved successfully.',
            })
            to_email = user.email
            email = EmailMessage(
                subject, message, to=[to_email]
            )
            email.content_subtype = "html"
            email.send()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def decline(self, request, pk, format=None):
        profile = self.get_object()
        serializer = ServiceProviderApprovalSerializer(
            profile, data=request.data)
        if serializer.is_valid():
            serializer.save(status='Rejected', approved_date=datetime.datetime.now(
            ), approver=self.request.user)
            # sending message to the service provider for notification
            user = profile.user
            current_site = get_current_site(request)
            subject = 'Your application has been Declined'
            message = render_to_string('farm_created_successful_email.html', {
                'user': user,
                'domain': current_site.domain,
                'message': 'Your application as a service provider has been declined.',
            })
            to_email = user.email
            email = EmailMessage(
                subject, message, to=[to_email]
            )
            email.content_subtype = "html"
            email.send()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def create(self, request, format=None):
        serializer = PostServiceProviderSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.status = 'Pending'
                #serializer.user = self.request.user
                serializer.save(user=self.request.user)
            except IntegrityError:
                return Response({'error': 'Service Provider account already exists'})

            return Response({'status': 'successful'})
        return Response(serializer.errors, status=400)


class ServiceProviderList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'serviceprovider_list.html'

    def get(self, request):
        queryset = ServiceProvider.objects.order_by('service_type')
        return Response({'serviceproviders': queryset})

# View for creating a service


class CreateServiceView(LoginRequiredMixin, CreateView):
    template_name = 'register_service.html'
    success_url = reverse_lazy('openmarket:serviceregistration_list')
    form_class = ServiceProfileForm
    success_message = "Your profile was created successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(CreateServiceView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateServiceView, self).get_form_kwargs()
        kwargs['request'] = self.request
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
        form.save_m2m()

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


# views for service registration

class ServiceRegistrationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    #queryset = Service.objects.all().order_by('service_name')
    serializer_class = ServiceRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the services 
        for the currently authenticated user.
        """
        user = self.request.user
        services = Service.objects.order_by('-id')
        lon = self.request.query_params.get('lon', None)
        lat = self.request.query_params.get('lat', None)

        if self.request.user.is_superuser or self.request.user.has_perm('openmarket.view_service'):
            if lat is not None and lon is not None:
                user_location = Point(float(lon), float(lat), srid=4326)
                print(user_location)
                queryset = Service.objects.annotate(distance=Distance(
                    "location", user_location)).order_by('distance')
            else:

                queryset = services
        else:
            queryset = services.filter(user=user)

        return queryset

    def create(self, request, format=None):
        serializer = PostServiceRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            try:
                #     serializer.status ='Pending'
                #serializer.user = self.request.user
                serializer.save(user=self.request.user)
            except IntegrityError:
                return Response({'error': 'Service account already exists'})

            return Response({'status': 'successful'})
        return Response(serializer.errors, status=400)


class MapServiceDetailView(DetailView):
    model = Service
    template_name = "map_service_detail.html"

    def get_context_data(self, **kwargs):
        context = super(MapServiceDetailView, self).get_context_data(**kwargs)
        context['Serviceobject'] = self.object

        return context


# service provider list
class ServiceProviderProfileList(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'serviceprovider_list.html'

    def get(self, request):
        queryset = ServiceProvider.objects.order_by('region')
        return Response({'serviceproviders': queryset})


# views for creating a service provider profile

class CreateServiceProviderProfile(LoginRequiredMixin, CreateView):
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
        form.save_m2m()

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



class ServiceRegistrationList(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'serviceregistration_list.html'
    #context_object_name = "servicerecord"

    def get(self, request):
        return Response()


# views for ContactDetails
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


# views for Logistics
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


# views for packaging
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


# update service provider view
class UpdateServiceProviderProfile(LoginRequiredMixin, UpdateView):
    model = ServiceProvider
    template_name = 'register_service_provider.html'
    success_url = reverse_lazy('openmarket:service_registration')
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
        form.save_m2m()

        return redirect('openmarket:serviceprovider_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


# Service Provider Detail View
class ServiceProviderProfileDetailView(LoginRequiredMixin, DetailView):
    model = ServiceProvider
    context_object_name = "providerrecord"
    template_name = "view_service_provider_profile.html"

   
    def get_context_data(self, **kwargs):
        #serviceprovider = ServiceProvider.objects.create(user=kwargs['instance'].user)
        context = super(ServiceProviderProfileDetailView,
                        self).get_context_data(**kwargs)

        context['providerrecord'] = self.object
        #context['servicerecord'] = Service.objects.filter(user = self.object)
        return context


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Service
    context_object_name = "servicerecord"

    template_name = "view_services_details.html"

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)

        context.update({

        })
        return context


class EditServiceView(LoginRequiredMixin, UpdateView):
    model = Service
    template_name = 'register_service.html'
    success_url = reverse_lazy('openmarket:serviceregistration_list')
    form_class = ServiceProfileForm
    success_message = "Service has been updated successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(EditServiceView, self).dispatch(request, *args, **kwargs)

    # def get_form_kwargs(self, request, *args, **kwargs):

    #     kwargs['request'] = self.request

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
        return self.form_invalid(form)

    def form_valid(self, form):
        farm = form.save(commit=False)
        farm.save()

        # send email to farmer  a message after an update
        return redirect('openmarket:serviceregistration_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


#Edit seller View
class EditSellerView(LoginRequiredMixin, UpdateView):
    model = Seller
    template_name = 'create_seller_profile.html'
    success_url = reverse_lazy('openmarket:seller_list')
    form_class = SellerProfileForm
    success_message = "Seller Profile has been updated successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(EditSellerView, self).dispatch(request, *args, **kwargs)

    # def get_form_kwargs(self, request, *args, **kwargs):

    #     kwargs['request'] = self.request

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            print(form.errors)
        return self.form_invalid(form)

    def form_valid(self, form):
        farm = form.save(commit=False)
        farm.save()

        # send email to farmer  a message after an update
        return redirect('openmarket:seller_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))

# seller post
class CreateSellerPost(CreateView):
    template_name = 'create_seller_post.html'
    success_url = reverse_lazy('openmarket:sellerpost_list')
    form_class = SellerPostForm
    success_message = "Product was created successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(CreateSellerPost, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateSellerPost, self).get_form_kwargs()
        
        
        
        
        kwargs['request'] = self.request
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
        product = form.save(commit=False)
        product.seller = self.request.user
        product.save()
        return redirect('openmarket:sellerpost_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))

# seller post
class CreateBuyerPost(CreateView):
    template_name = 'create_buyer_post.html'
    success_url = reverse_lazy('openmarket:buyerpost_list')
    form_class = BuyerPostForm
    success_message = "Product was created successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(CreateBuyerPost, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateBuyerPost, self).get_form_kwargs()
        kwargs['request'] = self.request
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
        return redirect('openmarket:buyerpost_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


# update product view
class EditSellerPostView(LoginRequiredMixin, UpdateView):
    model = SellerPost
    template_name = 'create_seller_post.html'
    success_url = reverse_lazy('openmarket:sellerpost_list')
    form_class = SellerPostForm
    success_message = "Product has been updated successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(EditSellerPostView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditSellerPostView, self).get_form_kwargs()
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
        product = form.save(commit=False)
        product.save()
        return redirect('openmarket:sellerpost_list')

# load products with in a specific market selected

def load_products(request):
    market_id = request.GET.get('market')
    products = MarketPrice.objects.filter(market_id=market_id).order_by('-min_price')
    return render(request, 'products_dropdown_list_options.html', {'products': products})

