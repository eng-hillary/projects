from django.shortcuts import render
from .models import (Sector, Enterprise, Farm)
from .serializers import (SectorSerializer, EnterpriseSerializer, FarmSerializer
,FarmMapSerializer)
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.urls import reverse_lazy
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)
from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
from .forms import (FarmForm,EnterpriseForm)
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from farmer .models import FarmerProfile

# views for sector
class SectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = Sector.objects.all().order_by('-id')
    serializer_class = SectorSerializer
    permission_classes = [permissions.IsAuthenticated]


class SectorList(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sector_list.html'

    def get(self, request):
       # queryset = Sector.objects.order_by('-id')
        return Response()


class SectorDetail(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sector_detail.html'
    context_object_name = "sectorrecord"

    def get(self, request, pk):
        sector = get_object_or_404(Sector, pk=pk)
        serializer = SectorSerializer(sector)
        return Response({'serializer': serializer, 'sector': sector})

    def post(self, request, pk):
        sector = get_object_or_404(Sector, pk=pk)
        serializer = SectorSerializer(sector, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'sector': sector})
        serializer.save()
        return redirect('farms:sector_list')


class CreateSector(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create_sector.html'

    def get(self, request):
        sector = None
        serializer = SectorSerializer()
        return Response({'serializer': serializer, 'sector': sector})

    def post(self, request):
        serializer = SectorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('farm:sector_list')

# views for enterprise
class EnterpriseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sectors to be viewed or edited.
    """
    queryset = Enterprise.objects.all().order_by('farm')
    serializer_class = EnterpriseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the farms 
        for the currently authenticated user.
        """
        user = self.request.user
        farmer = FarmerProfile.objects.get(user=user)
        farms = Farm.objects.filter(farmer =farmer)
        enterprises = Enterprise.objects.all().order_by('farm')
        if self.request.user.is_superuser or self.request.user.groups.filter(name='UNFFE Agents').exists():
            queryset = enterprises
        else:
            queryset = enterprises.filter(farm__in=farms)
        
        return queryset


class EnterpriseList(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'enterprise_list.html'

    def get(self, request):
        queryset = Enterprise.objects.order_by('-id')
        return Response({'enterprise': queryset})



# farm api viewset
class FarmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    serializer_class = FarmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the farms 
        for the currently authenticated user.
        """
        user = self.request.user
        farmer = FarmerProfile.objects.get(user=user)
        farms = Farm.objects.all().order_by('farmer')
        if self.request.user.is_superuser or self.request.user.groups.filter(name='UNFFE Agents').exists():
            queryset = farms
        else:
            queryset = farms.filter(farmer=farmer)
        
        return queryset


# farm api for maps
class FarmMapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = Farm.objects.all()
    serializer_class = FarmMapSerializer
    



# list of farms
class FarmListView(APIView, LoginRequiredMixin):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'farm_list.html'

    def get(self, request):
        return Response()



# create farm 
class CreateFarmView(LoginRequiredMixin,CreateView):
    template_name = 'create_farm.html'
    success_url = reverse_lazy('farm:farm_list')
    form_class = FarmForm
    success_message = "Farm has been created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateFarmView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateFarmView, self).get_form_kwargs()
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
        farm = form.save(commit=False)
        # assign total land to available land
        farm.available_land = farm.land_occupied
        farm.save()

        # send email to farmer after registration
        current_site = get_current_site(self.request)
        subject = 'Farm Created Successfully'
        message = render_to_string('farm_created_successful_email.html', {
            'user': farm.farmer.user,
            'domain': current_site.domain,
            'message': 'Your '+farm.name + ' has been registered sucessfully',
            })
        to_email = farm.farmer.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
        email.send()
        return redirect('farm:farm_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))


# update farm view
class EditFarmView(LoginRequiredMixin,UpdateView):
    model =Farm
    template_name = 'create_farm.html'
    success_url = reverse_lazy('farm:farm_list')
    form_class = FarmForm
    success_message = "Farm has been updated successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(EditFarmView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditFarmView, self).get_form_kwargs()
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

         # send email to farmer  a message after an update
        current_site = get_current_site(self.request)
        subject = 'Farm Updated Successfully'
        message = render_to_string('farm_created_successful_email.html', {
            'user': farm.farmer.user,
            'domain': current_site.domain,
            'message': 'Your '+farm.name + ' Details have been updated sucessfully',
            })
        to_email = farm.farmer.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
        email.send()
        return redirect('farm:farm_list')


    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))



# create enterprise
class CreateEnterpriseView(LoginRequiredMixin,CreateView):
    template_name = 'create_enterprise.html'
    success_url = reverse_lazy('farm:farm_list')
    form_class = EnterpriseForm
    success_message = "Farm has been created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateEnterpriseView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateEnterpriseView, self).get_form_kwargs()
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
        enterprise = form.save(commit=False)
        enterprise.save()
        # calculating remaining land on the farm
        # get the farm first
        farm = Farm.objects.get(id=enterprise.farm_id)
        farm_land_occupied = farm.land_occupied
        # subtracting the enterprise land from the farm land
        farm_available_land = farm_land_occupied - enterprise.land_occupied
        # update the farm object
        Farm.objects.filter(id=enterprise.farm_id).update(available_land=farm_available_land)
        print(farm_available_land)
        # send email to farmer after registration
        current_site = get_current_site(self.request)
        subject = 'Enterprise Created Successfully'
        message = render_to_string('enterprise_email.html', {
            'user': enterprise.farm.farmer.user,
            'domain': current_site.domain,
            'message': 'Your '+enterprise.name + ' has been registered sucessfully',
            })
        to_email = enterprise.farm.farmer.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
        email.send()
        return redirect('farm:enterprise_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_initial(self, *args, **kwargs):
        initial = super(CreateEnterpriseView, self).get_initial(**kwargs)
        initial['farm'] = Farm.objects.get(pk=self.kwargs['farm_pk'])
        return initial

    def get_context_data(self, **kwargs):
        context = super(CreateEnterpriseView, self).get_context_data(**kwargs)
        farm = Farm.objects.get(pk=self.kwargs['farm_pk'])
        context['landsize'] = farm.land_occupied
        context['available_land'] = farm.available_land
        return context


# update Enterprise view
class EditEnterpriseView(LoginRequiredMixin,UpdateView):
    model =Enterprise
    template_name = 'create_enterprise.html'
    success_url = reverse_lazy('farm:farm_list')
    form_class = EnterpriseForm
    success_message = "Enterprise has been updated successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(EditEnterpriseView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditEnterpriseView, self).get_form_kwargs()
        kwargs['request'] = self.request
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
        enterprise = form.save(commit=False)
        enterprise.save()

         # send email to farmer  a message after an update
        current_site = get_current_site(self.request)
        subject = 'Enterprise Updated Successfully'
        message = render_to_string('enterprise_email.html', {
            'user': enterprise.farm.farmer.user,
            'domain': current_site.domain,
            'message': 'Your '+enterprise.name + ' Details have been updated sucessfully',
            })
        to_email = enterprise.farm.farmer.user.email
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.content_subtype = "html"
        email.send()
        return redirect('farm:enterprise_list')


    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))