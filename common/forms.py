from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

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

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Insert a valid email address.')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
   
  
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email','password', 'password2']
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
      