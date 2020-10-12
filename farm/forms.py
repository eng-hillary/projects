from .models  import Farm, Enterprise, Sector, PestAndDisease
from django import forms
from farmer.models import FarmerProfile



class FarmForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Farm
        exclude = ['status','available_land']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FarmForm, self).__init__(*args, **kwargs)
        self.fields['general_remarks'].widget.attrs.update({'rows': '2'})
      
class QueryForm(forms.ModelForm):
    date_discovered = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    reporting_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = PestAndDisease
        exclude = ['solution']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(QueryForm, self).__init__(*args, **kwargs)
        self.fields['action_taken'].widget.attrs.update({'rows': '2'})
      

      
class EnterpriseForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    from_period = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    to_period = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Enterprise
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EnterpriseForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '2'})
        self.fields['farm'].empty_label = None
        self.fields['sector'].empty_label = '--please select--'
        farmersectors = FarmerProfile.objects.filter(user=self.request.user).values('sector')
        self.fields['sector'].queryset = Sector.objects.filter(id__in=farmersectors)