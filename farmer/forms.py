from django import forms
from .models import FarmerProfile
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class FarmerProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone_1 = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True, initial='+256')
    phone_2 = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True, initial='+256')
    

    class Meta:
        model = FarmerProfile
        exclude = ['user','status','status','approver','approved_date']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FarmerProfileForm, self).__init__(*args, **kwargs)
       