from .models  import Resource, ResourceBooking
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.gis import forms 
from django.contrib.gis.geos import Point



class ResourceForm(forms.ModelForm):
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500, 'mouse_position': True,'default_zoom':7}),
     initial=Point(y=1.0609637, x=32.5672804, srid=4326))
    Phone_number1 = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True, initial='+256')
    Phone_number2 = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=False, initial='+256')
    available_from = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    available_to = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    class Meta:
        model = Resource
        exclude = ['owner']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ResourceForm, self).__init__(*args, **kwargs)
        self.fields['terms_and_conditions'].widget.attrs.update({'rows': '3'})
      
class ResourceBookingForm(forms.ModelForm):
    date_needed = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
   
    class Meta:
        model = ResourceBooking
        exclude = ['booker']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ResourceBookingForm, self).__init__(*args, **kwargs)

class ResourceListForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['resource_name','owner','Phone_number1','price']
       
    