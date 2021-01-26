from django import forms

from .models import Seller,Product,ServiceProvider, Service, Category,SellerPost, BuyerPost


from .models import Seller,Product,ServiceProvider, Service, Category,SellerPost

from common.models import Region, District, County, SubCounty, Parish, Village
from common.choices import SERVICE_CATEGORY
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.gis import forms 
from django.contrib.gis.geos import Point
from unffeagents.models import Market, MarketPrice

from decimal import Decimal

from django.forms.models import inlineformset_factory



class ServiceProviderProfileForm(forms.ModelForm):
   
    
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

        self.fields['business_address'].widget.attrs.update({'rows': '2'})

class ProductProfileForm(forms.ModelForm):
    
     class Meta:
        model = Product
        exclude = ['date_created', 'date_updated','seller']

     def __init__(self, *args, **kwargs):
         self.request = kwargs.pop('request', None)
         super(ProductProfileForm, self).__init__(*args, **kwargs)
         self.fields['description'].widget.attrs.update({'rows': '2'})
         self.fields['category'].empty_label = '--please select--'

class ServiceProfileForm(forms.ModelForm):
    availability_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500, 'mouse_position': True,'default_zoom':7}),
     initial=Point(y=1.0609637, x=32.5672804, srid=4326))

    class Meta:
        model = Service
        exclude = ['date_created', 'date_updated','user','serviceprovider']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ServiceProfileForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = '--please select--'
        # servicecategories = ServiceProvider.objects.filter(user=self.request.user).values('category')
        # self.fields['category'].queryset = Category.objects.filter(id__in = servicecategories)


class SellerPostForm(forms.ModelForm):
    market = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Market.objects.all())
    product = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), queryset=Market.objects.none())


    class Meta:
        model = SellerPost
        exclude = ['seller']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SellerPostForm, self).__init__(*args, **kwargs)
        user = self.request.user
        self.fields['market'].empty_label = '--please select--'
        self.fields['product'].empty_label = '--please select--'
        self.fields['product_description'].widget.attrs.update({'rows': '2'})

        if 'market' in self.data:
            try:
                market_id = int(self.data.get('market'))
                self.fields['product'].queryset = MarketPrice.objects.filter(market_id=market_id).order_by('-min_price')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty district queryset
        elif self.instance.pk:
            self.fields['product'].queryset = self.instance.market.marketprice_set.order_by('-min_price')
    
    def clean_price_offer(self):
        price_offer = Decimal(self.cleaned_data['price_offer'])
        price_range = self.cleaned_data.get('product')
        print(price_range)
        prices = str(price_range).split()
        splitted_prices = prices[-1]
        actual_prices = splitted_prices.split("-")
        max_price = Decimal(actual_prices[1])
        min_price = Decimal(actual_prices[0])
       
        if not min_price <= price_offer <= max_price:
            raise forms.ValidationError("Please enter a price within the product price range")
        return price_offer


class BuyerPostForm(forms.ModelForm):

    class Meta:
        model = BuyerPost
        exclude = []

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(BuyerPostForm, self).__init__(*args, **kwargs)
        user = self.request.user
        self.fields['product'].empty_label = '--please select--'
 

class MarketPriceForm(forms.ModelForm):
    class Meta:
        model = MarketPrice
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(MarketPriceForm, self).__init__(*args, **kwargs)
        self.fields['market'].empty_label = '--please select--'
        self.fields['product'].empty_label = '--please select--'
       