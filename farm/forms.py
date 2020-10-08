from .models  import Farm, Enterprise
from django import forms



class FarmForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Farm
        exclude = ['status','available_land']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FarmForm, self).__init__(*args, **kwargs)
        self.fields['general_remarks'].widget.attrs.update({'rows': '2'})
      

      
class EnterpriseForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Enterprise
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EnterpriseForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'rows': '2'})
        self.fields['farm'].empty_label = None
        self.fields['enterprise_type'].empty_label = '--please select--'