from django import forms
from .models import Seller,Product,ServiceProvider, Service
from common.models import Region, District
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget



class ServiceProviderProfileForm(forms.ModelForm):
    #date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone_1 = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True, initial='+256')
    phone_2 = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=False, initial='+256')
    
    class Meta:
        model = ServiceProvider
        exclude = ['user','status','status','approver','approved_date']

 
class SellerProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    business_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True, initial='+256')
    
    
    class Meta:
        model = Seller
        exclude = ['user','status', 'approver','approved_date']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SellerProfileForm, self).__init__(*args, **kwargs)
        self.fields['district'].empty_label = '--please select--'
        self.fields['region'].empty_label = '--please select--'
        self.fields['county'].empty_label = '--please select--'
        self.fields['sub_county'].empty_label = '--please select--'
        self.fields['parish'].empty_label = '--please select--'
        self.fields['village'].empty_label = '--please select--'
        self.fields['enterprise'].empty_label = '--please select--'
        self.fields['major_products'].empty_label = '--please select--'

class ProductProfileForm(forms.ModelForm):
    
     class Meta:
        model = Product
        exclude = ['date_created', 'date_updated']

     def __init__(self, *args, **kwargs):
         self.request = kwargs.pop('request', None)
         super(ProductProfileForm, self).__init__(*args, **kwargs)

class ServiceProfileForm(forms.ModelForm):
    
     class Meta:
        model = Service
        exclude = ['date_created', 'date_updated']

     def __init__(self, *args, **kwargs):
         self.request = kwargs.pop('request', None)
         super(ServiceProfileForm, self).__init__(*args, **kwargs)
