from django.views.generic import (
    CreateView, UpdateView, DetailView, TemplateView, View, DeleteView)
from django.http import (HttpResponseRedirect,JsonResponse, HttpResponse,
                         Http404)

from .forms import LoginForm, SignUpForm, ProfileForm
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


class HomePage(TemplateView):

    template_name = 'home.html'

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


# sign up method
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            profile_form = ProfileForm(request.POST, instance=user)
            profile_form.save_m2m()
            
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('common:account_activation_sent')
    # else:
    #     print(form.errors)
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'form': form, 'profile_form':profile_form})


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
        user.email_confirmed = True
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
