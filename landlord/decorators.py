from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse('<center><b>sorry you are not allow to view this page</b></center>')

        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request,*args,**kwargs):
        groups = None
        if request.user.groups.exist():
            groups = request.user.groups.all()[0].name

            if group == 'tenant':
                return redirect('tenant-home')
            elif group == 'admin':
                return view_func(request,*args,**kwargs)
    wrapper_func
