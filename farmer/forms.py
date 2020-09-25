from django import forms
from .models import FarmerProfile
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from common .models import(District, County, SubCounty, Parish, Village)


class FarmerProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone_1 = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True, initial='+256')
    phone_2 = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=False, initial='+256')


    class Meta:
        model = FarmerProfile
        exclude = ['user','status','approver','approved_date']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FarmerProfileForm, self).__init__(*args, **kwargs)
        self.fields['general_remarks'].widget.attrs.update({'rows': '2'})
        self.fields['district'].empty_label = '--please select--'
        self.fields['district'].queryset = District.objects.none()
        self.fields['region'].empty_label = '--please select--'
        self.fields['county'].empty_label = '--please select--'
        self.fields['county'].queryset = County.objects.none()
        self.fields['sub_county'].empty_label = '--please select--'
        self.fields['sub_county'].queryset = SubCounty.objects.none()
        self.fields['parish'].empty_label = '--please select--'
        self.fields['parish'].queryset = Parish.objects.none()
        self.fields['village'].empty_label = '--please select--'
        self.fields['village'].queryset = Village.objects.none()
        self.fields['group'].empty_label = '--please select--'

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['district'].queryset = District.objects.filter(region_id=region_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty district queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.Region.district_set.order_by('name')

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['county'].queryset = County.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty district queryset
        elif self.instance.pk:
            self.fields['county'].queryset = self.instance.District.county_set.order_by('name')
        
        if 'county' in self.data:
            try:
                county_id = int(self.data.get('county'))
                self.fields['sub_county'].queryset = SubCounty.objects.filter(county_id=county_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty district queryset
        elif self.instance.pk:
            self.fields['sub_county'].queryset = self.instance.County.sub_county_set.order_by('name')

        
        if 'sub_county' in self.data:
            try:
                sub_county_id = int(self.data.get('sub_county'))
                self.fields['parish'].queryset = Parish.objects.filter(sub_county_id=sub_county_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty district queryset
        elif self.instance.pk:
            self.fields['parish'].queryset = self.instance.SubCounty.parish_set.order_by('name')


        if 'parish' in self.data:
            try:
                parish_id = int(self.data.get('parish'))
                self.fields['village'].queryset = Village.objects.filter(parish_id=parish_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty district queryset
        elif self.instance.pk:
            self.fields['village'].queryset = self.instance.Parish.village_set.order_by('name')