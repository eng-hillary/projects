from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import Owner,House
from django.contrib.auth.models import User

class CreatOwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['fname','lname','email','address','contact','picture']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class UpdateProfile(ModelForm):
    class Meta:
        model =  Owner
        fields = ['contact','email','address','picture']

class AddHouseForm(ModelForm):
    class Meta:
        model = House
        fields = ['category','location','address','rooms','picture','price','description']