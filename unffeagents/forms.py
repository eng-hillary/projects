from django import forms
from .models import AgentProfile, Notice
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from common .models import (Region)
from farm .models import Sector
from django.shortcuts import render
from django.utils.safestring import mark_safe

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



class NoticeForm(forms.ModelForm):
    display_up_to = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
  
        
    class Meta:
        model = Notice
        exclude = ['posted_by']

    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '3'})
        self.fields['sector'].empty_label = None
        self.fields['region'].empty_label = None
        self.fields['sector'].widget = forms.CheckboxSelectMultiple()
        self.fields['region'].widget = forms.CheckboxSelectMultiple()
       