from django.shortcuts import render
from .models import (AgentProfile, Market, MarketPrice, Notice,CallRsponse,Call)
from .serializers import (AgentProfileSerializer,ProductOrderingSerializer, MarketSerializer, MarketPriceSerializer, 
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
from .forms import (AgentProfileForm,ProductOrderingForm, NoticeForm,EnquiryForm, MarketForm, MarketPriceForm)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from django.contrib import messages
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)

from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
from rest_framework import filters
from django.contrib.auth.models import User, Group
import requests
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from openmarket.models import SellerPost,ProductCategory,Product, ProductOrdering
from django.db import IntegrityError

# views for agentprofiles
class AgentProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows agent profiles to be viewed or edited.
    To post the body must contain 
        {
        "user": "1",//the user profile of the agent
        "contact": "+256788329636", //contact with the country code
        "region": "1", //region of the agent
        "district": "1", // District where the agent is located
        "specific_role": "call centre agent",options['account manager','market manager','call centre agent','notifications and alerts']
      
    }
    """
    #queryset = AgentProfile.objects.all().order_by('specific_role')
    serializer_class = AgentProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the agent profiles
        for the currently authenticated user.
        """
        user = self.request.user
        agents = AgentProfile.objects.all().order_by('-user')
        if  self.request.user.has_perm('unffeagents.delete_agentprofile'):
            queryset = agents
        else:
            queryset = agents.filter(user=user)
        
        return queryset
    """
    Retrieve, update or delete a snippet an agent.
    """
    # def get_object(self, pk):
    #     try:
    #         return AgentProfile.objects.get(pk=pk)
    #     except AgentProfile.DoesNotExist:
    #         raise Http404


    def create(self, request, format=None):
        serializer = PostAgentProfileSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save(user = self.request.user)
                serializer.save()
            except IntegrityError:
                return Response({'error':'Agent account already exists'})
                
            return Response({'status':'successful'})
        return Response(serializer.errors, status=400)
    
    def update(self, request,pk,format=None):
        """
        get the object
        """
        try:
            agent = AgentProfile.objects.get(pk=pk)
        except AgentProfile.DoesNotExist:
            raise Http404
        """Updating the object"""
        serializer = PostAgentProfileSerializer(agent,data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response({'error':'An error has occured'})
                
            return Response({'status':'successful updated'})
        return Response(serializer.errors, status=404)
    

    def delete(self, request, pk, format=None):
        try:
            agent = AgentProfile.objects.get(pk=pk)
        except AgentProfile.DoesNotExist:
            raise Http404

        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, pk, format=None):
        try:
            agent = AgentProfile.objects.get(pk=pk)
        except AgentProfile.DoesNotExist:
            raise Http404
        serializer = AgentProfileSerializer(agent)
        return Response(serializer.data)


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
        profile.save()

        # send email to farmer after registration
        current_site = get_current_site(self.request)
        subject = 'Registrated Successful'
        message = render_to_string('profile_created_successful.html', {
            'user': profile.user,
            'domain': current_site.domain,
            'message':'Your Agent account has been successfully created'
            })
        to_email = profile.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
        email.send()
        return redirect('unffeagents:agentprofile_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))



# update farm view
class EditAgentProfileView(LoginRequiredMixin,UpdateView):
    model =AgentProfile
    template_name = 'create_agentprofile.html'
    success_url = reverse_lazy('unffeagents:agentprofile_list')
    form_class = AgentProfileForm
    success_message = "Your profile was edit successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(EditAgentProfileView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditAgentProfileView, self).get_form_kwargs()
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
        profile.save()

          # send email to farmer after registration
        current_site = get_current_site(self.request)
        subject = 'Registrated Successful'
        message = render_to_string('profile_created_successful.html', {
            'user': profile.user,
            'domain': current_site.domain,
            'message':'Your Agent account has been successfully updated'
            })
        to_email = profile.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
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
    #queryset = Market.objects.all().order_by('market_name')
    serializer_class = MarketSerializer
   # permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """
      returns markets nearest to the user in case you pass in logitude and lat
        """
        lon = self.request.query_params.get('lon', None)
        lat = self.request.query_params.get('lat', None)

        if lat is not None and lon is not None:
                user_location = Point(float(lon), float(lat), srid=4326)
                queryset = Market.objects.annotate(distance=Distance(
                    "location", user_location)).order_by('distance')
        else:
            queryset = Market.objects.all().order_by('market_name')
     

        return queryset


class MarketDetailView(DetailView):
    model = Market
    template_name = "view_market_detail.html"

    def get_context_data(self, **kwargs):
        context = super(MarketDetailView, self).get_context_data(**kwargs)
        context['Marketobject'] = self.object
        products = SellerPost.objects.filter(market=self.object)
        print(products)
        context["products"]= products
        context["categories"] = ProductCategory.objects.all()
        print(products)
        
        return context

class ProductDetailView(DetailView):
    model = SellerPost
    template_name = "view_product_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['Productobject'] = self.object
        
        return context
        
class MarketList(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'market_list.html'

    def get(self, request):
        queryset = Market.objects.order_by('-id')
        return Response({'markets': queryset})



class ProductOrderingList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'productordering_list.html'

    def get(self, request):
        queryset = ProductOrdering.objects.order_by('product')
        return Response({'productorderings': queryset})

class ProductOrderingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resources to be viewed or edited.
    """
    queryset = ProductOrdering.objects.all()
    serializer_class = ProductOrderingSerializer


# create booking
class ProductOrderingView(CreateView):
    template_name = 'ordering.html'
    success_url = reverse_lazy('unffeagents:productordering_list')
    form_class = ProductOrderingForm
    success_message = "Ordering has been created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(ProductOrderingView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ProductOrderingView, self).get_form_kwargs()
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
        product.buyer = self.request.user
        product.save()
        
        print(product.product.seller.user.email)

        # send email to seller after registration
        current_site = get_current_site(self.request)
        subject = 'Order successfully Successfully'
        message = render_to_string('booking_created_successfully_email.html', {
            'user': product.product.seller.user,
            'domain': current_site.domain,
            'product':product
            })
        to_email = product.product.seller.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
        email.send()
        messages.add_message(self.request, messages.INFO, 'Please wait for approval from the seller')
        return redirect('unffeagents:productordering_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))

    def get_initial(self, *args, **kwargs):
        initial = super(ProductOrderingView, self).get_initial(**kwargs)
        initial['product'] = SellerPost.objects.get(pk=self.kwargs['product_pk'])
        return initial

class CreateMarket(CreateView):
    template_name = 'create_market.html'
    form_class = MarketForm
    success_message = "Market was created successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(CreateMarket, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateMarket, self).get_form_kwargs()
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
        market = form.save(commit=False)
        market.save()
        return redirect('unffeagents:market_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))
  
# update market
# update product view
class EditMarketView(LoginRequiredMixin, UpdateView):
    model = Market
    template_name = 'create_market.html'
    success_url = reverse_lazy('unffeagents:market_list')
    form_class = MarketForm
    success_message = "Market has been updated successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(EditMarketView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditMarketView, self).get_form_kwargs()
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
        return redirect('unffeagents:market_list')


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



class CreateMarketPrice(CreateView):
    template_name = 'create_market_price.html'
    form_class = MarketPriceForm
    success_message = "Market Price  was posted successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(CreateMarketPrice, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateMarketPrice, self).get_form_kwargs()
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
        market = form.save(commit=False)
        market.user = self.request.user
        market.save()
        return redirect('unffeagents:marketprice_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))
  
# update market
# update product view
class EditMarketPriceView(LoginRequiredMixin, UpdateView):
    model = MarketPrice
    template_name = 'create_market_price.html'
    success_url = reverse_lazy('unffeagents:market_list')
    form_class = MarketPriceForm
    success_message = "Market Price has been updated successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(EditMarketPriceView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditMarketPriceView, self).get_form_kwargs()
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
        return redirect('unffeagents:marketprice_list')


# views for notices
class NoticeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notices to be viewed or edited.
    """
    queryset = Notice.objects.all().order_by('-created')
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
    queryset = Call.objects.order_by('-call_date')
    serializer_class = CallSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class CallList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'call_list.html'

    def get(self, request):
      
        return Response()


class EquiryList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'enquiry_list.html'

    def get(self, request):
      
        return Response()


class ResponseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = CallRsponse.objects.order_by('-id')
    serializer_class = ResponseSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['type_of_question','question','solution','called_from__name','caller','agent__first_name','agent__last_name']
    ordering_fields = '__all__'

# create notification
 
class CreateNoticeView(LoginRequiredMixin,CreateView):
    template_name = 'create_notification.html'
    success_url = reverse_lazy('unffeagents:notice_list')
    form_class = NoticeForm
    success_message = "Notice has been created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateNoticeView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateNoticeView, self).get_form_kwargs()
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
        notice = form.save(commit=False)
        notice.posted_by = self.request.user
        notice.save()
        form.save_m2m()
        users = []
        print(notice.sector.all())
        if notice.sector.all().count()>0:
            users =  User.objects.filter(is_active=True, farmer__isnull=False).exclude(email='')
            for user in users:
                if user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.region.filter(id=user.profile.region.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.district.filter(id=user.profile.district.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.county.filter(id=user.profile.county.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.sub_county.filter(id=user.profile.sub_county.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.parish.filter(id=user.profile.parish.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.village.filter(id=user.profile.village.id):
                    # sending email with notifications
                    current_site = get_current_site(self.request)
                    subject = notice.notice_title
                    message = render_to_string('notice_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'message': notice.description,
                        })
                    to_email = user.email
                    email = EmailMessage(
                        subject, message, to=[to_email]
                        )
                    email.content_subtype = "html"
                    email.send()

                    #send sms
                    if user.profile.phone_number:
                        try:
                            request_type = "POST"
                            url = 'https://techguy.thinvoidcloud.com/api.php'
                            data = {'contacts': str(user.profile.phone_number),'message': notice.description,'username': 'ivr@unffeict4farmers.org','password': 'ccsrzwub'}
                            response = requests.request(request_type, url, data=data)
                            print(response)
                            print(user.profile.phone_number)
                        except:
                            print('unable to  send messages')
                            
                            
        else:
            users = User.objects.filter(is_active=True).exclude(email='')
            for user in users:
                
                if user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.region.filter(id=user.profile.region.id): #or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.district.filter(id=user.profile.district.id) or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.county.filter(id=user.profile.county.id) or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.sub_county.filter(id=user.profile.sub_county.id) or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.parish.filter(id=user.profile.parish.id) or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.village.filter(id=user.profile.village.id):
                    
                    current_site = get_current_site(self.request)
                    subject = notice.notice_title
                    message = render_to_string('notice_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'message': notice.description,
                        })
                    to_email = user.email
                    email = EmailMessage(
                        subject, message, to=[to_email]
                        )
                    email.content_subtype = "html"
                    email.send()

                     #send sms
                    if user.profile.phone_number:
                        try:
                            request_type = "POST"
                            url = 'https://techguy.thinvoidcloud.com/api.php'
                            data = {'contacts': str(user.profile.phone_number),'message': notice.description,'username': 'ivr@unffeict4farmers.org','password': 'ccsrzwub'}
                            response = requests.request(request_type, url, data=data)
                            print(user.profile.phone_number)
                            print(response)
                        except:
                            print('unable to  send messages')
                            

        return redirect('unffeagents:notice_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


class EditNoticeView(LoginRequiredMixin,UpdateView):
    model =Notice
    template_name = 'create_notification.html'
    success_url = reverse_lazy('unffeagents:farm_list')
    form_class = NoticeForm
    success_message = "Notice has been updated successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(EditNoticeView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditNoticeView, self).get_form_kwargs()
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
        notice = form.save(commit=False)
        notice.save()
        form.save_m2m()
        users = []
        print(notice.sector.all())
        if notice.sector.all().count()>0:
            users =  User.objects.filter(is_active=True, farmer__isnull=False).exclude(email='')
            for user in users:
                if user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.region.filter(id=user.profile.region.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.district.filter(id=user.profile.district.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.county.filter(id=user.profile.county.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.sub_county.filter(id=user.profile.sub_county.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.parish.filter(id=user.profile.parish.id) or user.farmer.sector.filter(id__in=notice.sector.all()).exists() and notice.village.filter(id=user.profile.village.id):
                    # sending email with notifications
                    current_site = get_current_site(self.request)
                    subject = notice.notice_title
                    message = render_to_string('notice_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'message': notice.description,
                        })
                    to_email = user.email
                    email = EmailMessage(
                        subject, message, to=[to_email]
                        )
                    email.content_subtype = "html"
                    email.send()

                    #send sms
                    if user.profile.phone_number:
                        try:
                            request_type = "POST"
                            url = 'https://techguy.thinvoidcloud.com/api.php'
                            data = {'contacts': str(user.profile.phone_number),'message': notice.description,'username': 'ivr@unffeict4farmers.org','password': 'ccsrzwub'}
                            response = requests.request(request_type, url, data=data)
                            print(response)
                            print(user.profile.phone_number)
                        except:
                            print('unable to  send messages')
                            
                            
        else:
            users = User.objects.filter(is_active=True).exclude(email='')
            for user in users:
                
                if user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.region.filter(id=user.profile.region.id): #or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.district.filter(id=user.profile.district.id) or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.county.filter(id=user.profile.county.id) or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.sub_county.filter(id=user.profile.sub_county.id) or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.parish.filter(id=user.profile.parish.id) or user.groups.filter(id__in=notice.target_audience.all()).exists() and notice.village.filter(id=user.profile.village.id):
                    
                    current_site = get_current_site(self.request)
                    subject = notice.notice_title
                    message = render_to_string('notice_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'message': notice.description,
                        })
                    to_email = user.email
                    email = EmailMessage(
                        subject, message, to=[to_email]
                        )
                    email.content_subtype = "html"
                    email.send()

                     #send sms
                    if user.profile.phone_number:
                        try:
                            request_type = "POST"
                            url = 'https://techguy.thinvoidcloud.com/api.php'
                            data = {'contacts': str(user.profile.phone_number),'message': notice.description,'username': 'ivr@unffeict4farmers.org','password': 'ccsrzwub'}
                            response = requests.request(request_type, url, data=data)
                            print(user.profile.phone_number)
                            print(response)
                        except:
                            print('unable to  send messages')
                            
        return redirect('unffeagents:notice_list')


    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))

# create inquiry view
class CreateEquiryView(LoginRequiredMixin,CreateView):
    template_name = 'create_enquiry.html'
    success_url = reverse_lazy('unffeagents:enquiries')
    form_class = EnquiryForm
    success_message = "Notice has been created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateEquiryView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateEquiryView, self).get_form_kwargs()
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
        call =  Call.objects.get(pk=self.kwargs['session_id'])
        enquiry = form.save(commit=False)
        enquiry.agent = self.request.user
        enquiry.caller = call.phone
        enquiry.call = call
        enquiry.save()
        return redirect('unffeagents:enquiries')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


class EditEquiryView(LoginRequiredMixin,UpdateView):
    model =CallRsponse
    template_name = 'create_enquiry.html'
    success_url = reverse_lazy('unffeagents:enquiries')
    form_class = EnquiryForm
    success_message = "Equiry has been updated successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(EditEquiryView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditEquiryView, self).get_form_kwargs()
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
        notice = form.save(commit=False)
        notice.save()                  
        return redirect('unffeagents:enquiries')


    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))
    

class UsersList(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'users_list.html'

    def get(self, request):
        queryset = User.objects.order_by('-id')
        phone=self.request.query_params.get('phone', None)
        if phone is not None:
            print(str(phone))
            # queryset = queryset.filter(
            #         profile__phone_number__icontains=self.request.query_params.get('phone'))
            queryset = User.objects.filter(profile__phone_number=str(phone))
           
        print(queryset)
        return Response({'users': queryset})

