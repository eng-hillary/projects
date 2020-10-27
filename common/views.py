from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)
from .forms import LoginForm, SignUpForm, PasswordResetEmailForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.utils.encoding import force_text
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.urls import reverse_lazy
from .models import (Profile, District, Region, County, SubCounty, Parish, Village)
from django.core.mail import EmailMessage
from django.contrib.auth.views import PasswordResetView
from rest_framework.views import APIView
from rest_framework import parsers, renderers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework import permissions
from .forms import ProfileForm
from farmer.views import FarmerProfile
from django.db.models import Count, Q
import json
from .serializers import (GroupSerializer, UserSerializer, DistrictSerializer,CountySerializer
,SubCountySerializer,ParishSerializer,VillageSerializer,UserPostSerializer,UserApiPost)
from rest_framework import filters
from django.core import serializers as django_serializers
from rest_framework import status



class HomePage(LoginRequiredMixin, TemplateView):

    template_name = 'home.html'

    
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        dataset = FarmerProfile.objects \
        .values('sector') \
        .annotate(credit_access_count=Count('sector', filter=Q(credit_access=True)),
                  no_credit_access_count=Count('sector', filter=Q(credit_access=False))) \
        .order_by('sector')
    
        categories = list()
        credit_access_series_data = list()
        no_credit_access_series_data = list()

#Looping through the created dataset from above
        for entry in dataset:
            categories.append('%s Farmers' % entry['sector'])
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
        context["dataset"]=dataset
        context["chart"] = json.dumps(chart)
        #context["credit.html"] = credit.html
        
            
        return context
        

# login view
class LoginView(TemplateView):
    template_name = "registration/login.html"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST, request=request)
        if form.is_valid():

            user = User.objects.filter(username=request.POST.get('username')).first()

            if user is not None:
                if user.is_active:
                    user = authenticate(username=request.POST.get(
                        'username'), password=request.POST.get('password'))

                    if user is not None:
                        login(request, user)
                        return HttpResponseRedirect('/')
                    return render(request, "registration/login.html", {
                        "error": True,
                        "message":
                            "Your username and password didn't match. \
                            Please try again."
                    })
                return render(request, "registration/login.html", {
                    "error": True,
                    "message":
                        "Your Account is inactive. Please Contact Administrator"
                })
            return render(request, "registration/login.html", {
                "error": True,
                "message":
                    "Your Account is not Found. Please Contact Administrator"
            })
        print(form.errors)
        return render(request, "registration/login.html", {
            "error": True,
            "message": "Your username and password didn't match. Please try again.",
            "form": form
        })

class LogoutView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        logout(request)
        request.session.flush()
        return redirect("login")


class SignUpView(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('common:account_activation_sent')
    form_class = SignUpForm
    success_message = "Your profile was created successfully"

    def dispatch(self, request, *args, **kwargs):
        return super(
            SignUpView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(SignUpView, self).get_form_kwargs()
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
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        profile = Profile()
        user.refresh_from_db()  # load the profile instance created by the signal
        Token.objects.get_or_create(user=user)
        profile.phone_number = form.cleaned_data.get('phone_number')
        profile.phone_2 = form.cleaned_data.get('phone_2')
        profile.region = form.cleaned_data.get('region')
        profile.district = form.cleaned_data.get('district')
        profile.county = form.cleaned_data.get('county')
        profile.sub_county = form.cleaned_data.get('sub_county')
        profile.parish = form.cleaned_data.get('parish')
        profile.village = form.cleaned_data.get('village')
        profile.home_address = form.cleaned_data.get('home_address')
        profile.gender = form.cleaned_data.get('gender')
        profile.profile_pic = form.cleaned_data.get('profile_pic')
        profile.user = user
        profile.save()
        current_site = get_current_site(self.request)
        subject = 'Activate Your Account'
        message = render_to_string('account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
            })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                subject, message, to=[to_email]
            )
        email.send()
        return redirect('common:account_activation_sent')

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return self.render_to_response(self.get_context_data(form=form))




def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')




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

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "signup.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context["user_obj"] = self.request.user
        return context

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "signup.html"
    success_url = reverse_lazy("common:home")

    def form_valid(self, form):
        user = form.save(commit=False)

        user.save()
        form.save_m2m()

        if self.request.is_ajax():
            data = {'success_url': reverse_lazy(
                'common:home'), 'error': False}
            return JsonResponse(data)
        return super(UpdateProfileView, self).form_valid(form)

    def form_invalid(self, form):
        response = super(UpdateProfileView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return response

    def get_form_kwargs(self):
        kwargs = super(UpdateProfileView, self).get_form_kwargs()
        kwargs.update({"request_user": self.request.user})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        context["user_obj"] = self.object
        context["user_form"] = context["form"]

        if "errors" in kwargs:
            context["errors"] = kwargs["errors"]
        return context

class ForgotPasswordView(PasswordResetView):
    template_name = "forgot_password.html"
    form_class = PasswordResetEmailForm
    email_template_name = 'password_reset_email.html'
    from_email = 'nonereply@unffe.org'



# used to obtain authentication token
class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        picture = None
        if user.profile.profile_pic:
            picture = user.profile.profile_pic.url
        else:
            picture = None

        return Response({'token': token.key,'created': created,'id':user.pk,'username':user.username, 'email':user.email,
            'first_name':user.first_name,'last_name':user.last_name,'profile_pic':picture
            })


obtain_auth_token = ObtainAuthToken.as_view()


'''
Am using these methods to load data for cascading dropdowns of districts, counties and others
'''
def load_districts(request):
    region_id = request.GET.get('region')
    districts = District.objects.filter(region_id=region_id).order_by('name')
    return render(request, 'destrict_dropdown_list_options.html', {'districts': districts})


def load_counties(request):
    district_id = request.GET.get('district')
    counties = County.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'county_dropdown_list_options.html', {'counties': counties})


def load_sub_counties(request):
    county_id = request.GET.get('county')
    sub_counties = SubCounty.objects.filter(county_id=county_id).order_by('name')
    return render(request, 'sub_county_dropdown_list_options.html', {'sub_counties': sub_counties})


def load_parishes(request):
    sub_county_id = request.GET.get('sub_county')
    parishes = Parish.objects.filter(sub_county_id=sub_county_id).order_by('name')
    return render(request, 'parish_dropdown_list_options.html', {'parishes': parishes})

def load_villages(request):
    parish_id = request.GET.get('parish')
    villages = Village.objects.filter(parish_id=parish_id).order_by('name')
    return render(request, 'village_dropdown_list_options.html', {'villages': villages})



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = '__all__'
    ordering_fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['username','first_name','last_name','email','profile__gender','profile__phone_number']
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        else:
            return UserPostSerializer
        return UserSerializer

    def get_queryset(self):
        users = User.objects.all()
        user = self.request.user
        if self.request.user.is_superuser or self.request.user.groups.filter(name='Admin').exists():
            queryset = users
        else:
            queryset = User.objects.filter(id=user.id)
        
        return queryset

    def create(self, request, format=None):
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer
            user.save()
            
             #send an email
            # user_object = User.objects.get(username =serializer.data['username'])
            # current_site = get_current_site(request)
            # subject = 'Activate Your Account'
            # message = render_to_string('account_activation_email.html', {
            #     'user': user_object,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user_object.id)),
            #     'token': account_activation_token.make_token(user_object),
            #     })
            # to_email = serializer.data['email']
            # email = EmailMessage(
            #     subject, message, to=[to_email]
            #     )
            # email.send()
            response = {'message':'account created successfully'}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistrictViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','region__name']
    ordering_fields = '__all__'


class CountyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = County.objects.all()
    serializer_class = CountySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','district__name']
    ordering_fields = '__all__'


class SubCountyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = SubCounty.objects.all()
    serializer_class = SubCountySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','county__name']
    ordering_fields = '__all__'


class ParishViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = Parish.objects.all()
    serializer_class = ParishSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','sub_county__name']
    ordering_fields = '__all__'


class VillageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name','parish__name']
    ordering_fields = '__all__'


class PostUserDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows farms to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserApiPost
    permission_classes = [permissions.IsAuthenticated]
    