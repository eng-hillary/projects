from .models  import Farm
from django import forms



class FarmForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Farm
        exclude = ['status']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(FarmForm, self).__init__(*args, **kwargs)
        self.fields['general_remarks'].widget.attrs.update({'rows': '2'})
        self.fields['sector'].empty_label = '--please select--'
        