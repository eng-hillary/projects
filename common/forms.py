from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from phonenumber_field.widgets import PhoneNumberPrefixWidget


# login form
class LoginForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password:
            if len(password) < 4:
                raise forms.ValidationError(
                    'Password must be at least 4 characters long!')
        return password

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")


        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user:
                if not self.user.is_active:
                    pass
                    # raise forms.ValidationError("User is Inactive")
            else:
                pass
                # raise forms.ValidationError("Invalid email and password")
        return self.cleaned_data

# sign up form

class SignUpForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True, label='Email/Phone Number')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),required=True)


    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password', 'password2']
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

class ProfileForm(forms.ModelForm):
    home_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 30}),
                                        required=False)
    phone_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True)

    class Meta:
        model = Profile
        fields = ('phone_number', 'home_address', 'gender')
