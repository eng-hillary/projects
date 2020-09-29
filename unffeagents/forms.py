from django import forms
from .models import AgentProfile
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class AgentProfileForm(forms.ModelForm):
    contact = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True, initial='+256')
    
    class Meta:
        model = AgentProfile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AgentProfileForm, self).__init__(*args, **kwargs)
        self.fields['district'].empty_label = '--please select--'
        self.fields['region'].empty_label = '--please select--'
        self.fields['specific_role'].empty_label = '--please select--'