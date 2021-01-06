from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import CreateUserForm,CreatOwnerForm,UpdateProfile,AddHouseForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
from .models import Owner,House
from messenger.models import *

# Create your views here.
@login_required(login_url='llogin')
@allowed_users(allowed_roles=['landlord'])
def landlordindex(request):
    return render(request,'landlord/index.html')

@login_required(login_url='llogin')
@allowed_users(allowed_roles=['landlord'])
def landlordhome(request):
    return render(request,'landlord/home.html')

@unauthenticated_user
def landlordregister(request):

        form = CreateUserForm()
        ownerform = CreatOwnerForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            ownerform = CreatOwnerForm(request.POST)
            if form.is_valid() and ownerform.is_valid():
                username = form.cleaned_data.get('username')
                password1 = form.cleaned_data.get('password1')
                password2 = form.cleaned_data.get('password2')
                usr = form.save()

                fname = ownerform.cleaned_data.get('fname')
                lname = ownerform.cleaned_data.get('lname')
                email = ownerform.cleaned_data.get('email')
                contact = ownerform.cleaned_data.get('contact')
                address = ownerform.cleaned_data.get('address')

                group = Group.objects.get(name='landlord')
                usr.groups.add(group)

                owner = Owner.objects.create(user=usr,
                                                fname=fname,
                                                lname=lname,
                                                email=email,
                                                address=address,
                                                contact=contact,

                                                )
                owner.save()
                messages.success(request,'account successfully created for '+username)
                return redirect('lhome')
            elif form.cleaned_data.get('password1') != form.cleaned_data.get('password2'): 
                messages.warning(request,'the two passwords did not match')
                return redirect('lregister')
            else:
                 messages.warning(request,'user already exist')

        context = {'form':form,'ownerform':ownerform}
        return render(request,'landlord/register.html',context)
    
@unauthenticated_user
def landlordloginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        current_user = authenticate(request,username=username,password=password)
        user = User.objects.filter(username=username)
        if current_user is not None:
            login(request,current_user)
            return redirect('lhome')
        else:
            messages.warning(request,'incorrect username or password')
            return redirect('llogin')
    return render(request,'landlord/login.html')


@login_required(login_url='llogin')
@allowed_users(allowed_roles=['landlord'])
def houselisting(request):
    owner = request.user.owner
    houses = House.objects.filter(owner=owner)
    return render(request,'landlord/houses.html',{'houses':houses})

def landlorduserlogout(request):
    logout(request)
    return redirect('llogin')

@login_required(login_url='llogin')
@allowed_users(allowed_roles=['landlord'])
def landlordviewprofile(request):
    return render(request,'landlord/profile.html')


@login_required(login_url='llogin')
@allowed_users(allowed_roles=['landlord'])
def landlordupdateProfile(request,id):
    user = request.user.owner
    
    profile = UpdateProfile(instance=user)

    if request.method == 'POST':
        profile = UpdateProfile(request.POST,request.FILES,instance=user)
        if profile.is_valid():
            profile.save()
            messages.success(request,'profile updated successfully!')
            return redirect('lprofile')

    context = {'profile':profile}
    return render(request,'landlord/updateprofile.html',{'profile':profile})


@login_required(login_url='llogin')
@allowed_users(allowed_roles=['landlord'])
def addhouse(request):
    form = AddHouseForm()
    owner = request.user.owner
    if request.method == 'POST':
        form = AddHouseForm(request.POST)
        if form.is_valid():
            
            category = form.cleaned_data.get('category')
            location = form.cleaned_data.get('location')
            address = form.cleaned_data.get('address')
            picture = form.cleaned_data.get('picture')
            price = form.cleaned_data.get('price')
            rooms = form.cleaned_data.get('rooms')
            description = form.cleaned_data.get('description')
            house = House.objects.create(
                owner = owner,
                category = category,
                location = location,
                rooms = rooms,
                address = address,
                picture = picture,
                price = price,
                description = description,
            )
            house.save()
            
            form.save()
            messages.success(request,'houes has been added successfully!')
            return redirect('lhome')
        else:
            messages.warning(request,f'unable to save {owner} location,something went wrong!')
            return redirect('add-house')
        
        
    context = {'form':form}
    return render(request,'landlord/addhouse.html',context)


@login_required(login_url='llogin')
@allowed_users(allowed_roles=['landlord'])
def messages(request):
    notifications = ApprovalMsg.objects.filter(owner=request.user.owner)
    return render(request,'landlord/messages.html',{'notifications':notifications})


    
