from django.shortcuts import render
from .models import (Resource, ResourceSharing, ResourceBooking)
from .forms import(ResourceForm)
from .serializers import ResourceSerializer, ResourceSharingSerializer, ResourceBookingSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
# views for resources
class ResourceList(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'resource_list.html'

    def get(self, request):
       # queryset = Sector.objects.order_by('-id')
        return Response()

# resourcesharing api for resourcess
class ResourceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows resources to be viewed or edited.
    """
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    


# create resource
class CreateResourceView(LoginRequiredMixin,CreateView):
    template_name = 'create_resource.html'
    success_url = reverse_lazy('resourcesharing:resource_list')
    form_class = ResourceForm
    success_message = "Resource has been created successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(CreateResourceView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(CreateResourceView, self).get_form_kwargs()
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
        resource = form.save(commit=False)
        resource.save()
        return redirect('resourcesharing:resource_list')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))



# update resource view
class EditResourceView(LoginRequiredMixin,UpdateView):
    model = Resource
    template_name = 'create_resource.html'
    success_url = reverse_lazy('resourcesharing:resource_list')
    form_class = ResourceForm
    success_message = "Resource has been updated successfully"


    def dispatch(self, request, *args, **kwargs):
        return super(EditResourceView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(EditResourceView, self).get_form_kwargs()
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
        resource = form.save(commit=False)
        resource.save()
        return redirect('resourcesharing:resource_list')



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

