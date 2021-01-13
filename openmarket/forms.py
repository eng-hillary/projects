from django import forms
from .models import Seller,Product,ServiceProvider, Service, Category,MajorProducts
from common.models import Region, District, County, SubCounty, Parish, Village
from common.choices import SERVICE_CATEGORY
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.gis import forms 
from django.contrib.gis.geos import Point
from django.forms.models import inlineformset_factory


class ServiceProviderProfileForm(forms.ModelForm):
   
    
    class Meta:
        model = ServiceProvider
        exclude = ['user','status','status','approver','approved_date']

 
class SellerProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    business_number = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True, initial='+256')
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500, 'mouse_position': True,'default_zoom':7}),
    initial=Point(y=1.0609637, x=32.5672804, srid=4326))

    
    class Meta:
        model = Seller
        exclude = ['user','status', 'approver','approved_date']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SellerProfileForm, self).__init__(*args, **kwargs)
      
class MajorProductsForm(forms.ModelForm):
    product_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    
    class Meta:
        model = MajorProducts
        fields = ['product_name']
        

MajorproductsFormSet = inlineformset_factory(Seller, MajorProducts,
                                                 form=MajorProductsForm, min_num=1,max_num=10,extra=0)


class ProductProfileForm(forms.ModelForm):
    
     class Meta:
        model = Product
        exclude = ['date_created', 'date_updated','seller']

     def __init__(self, *args, **kwargs):
         self.request = kwargs.pop('request', None)
         super(ProductProfileForm, self).__init__(*args, **kwargs)
         self.fields['description'].widget.attrs.update({'rows': '2'})

class ServiceProfileForm(forms.ModelForm):
    availability_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500, 'mouse_position': True,'default_zoom':7}),
     initial=Point(y=1.0609637, x=32.5672804, srid=4326))

    class Meta:
        model = Service
        exclude = ['date_created', 'date_updated','user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ServiceProfileForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = '--please select--'
        # servicecategories = ServiceProvider.objects.filter(user=self.request.user).values('category')
        # self.fields['category'].queryset = Category.objects.filter(id__in = servicecategories)
