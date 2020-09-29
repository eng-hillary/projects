from django.db import models
from django.contrib.auth.models import User
from common.models import(Region, District, County, SubCounty, Parish, Village, TimeStampedModel)
from common.choices import(GENDER_CHOICES,
                           MARITAL_STATUSES,REGISTER_STATUS,
                           STATUS,INVENTORY_STATUS, TYPE,
                           PAYMENT_MODE, 
                           PAYMENT_OPTIONS,
                           YES_OR_NO,
                           SERVICE_CATEGORY)
from django.core.validators import RegexValidator
from farm.models import Enterprise
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _

# Create your models here.phone_2 = PhoneNumberField(widget=PhoneNumberPrefixWidget(attrs={'class': 'form-control','style': 'width:50%; display:inline-block;'}), required=True, initial='+256')

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    enterprise = models.ForeignKey(to='farm.Enterprise',related_name='products',on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Seller(models.Model):
    #personal information
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    date_of_birth = models.DateField(max_length=8)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15)
    marital_status = models.CharField(choices=MARITAL_STATUSES, max_length=15, null=False, blank=False)
    seller_type = models.CharField(choices=TYPE,max_length=15, null=False)
    enterprise = models.ForeignKey(to='farm.Enterprise',on_delete=models.CASCADE)
    major_products = models.ForeignKey(Product, on_delete=models.CASCADE)

    #Location
    business_number = PhoneNumberField()
    business_location = models.CharField(null=True, max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    
    status = models.CharField(choices=REGISTER_STATUS, default='in_active', max_length=20,null=False)
      # handle approving of a seller
    approver = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name="seller_unffe_agent",null=True,blank=True)
    approved_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('seller_type',)
    def __str__(self):
        return self.seller_type

class Buyer(TimeStampedModel, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')
    
    class meta:
        ordering =("created")


class SellerPost(models.Model):
    name = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(max_length=50, null=True)
    price_offer = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_option = models.CharField(max_length=50)
    payment_options = models.CharField(choices=PAYMENT_OPTIONS, max_length=50, null=True)
    payment_mode = models.CharField(choices=PAYMENT_MODE, null=True, max_length=50)

    class Meta:
        ordering = ('-name',)
   

class BuyerPost(models.Model):
    name = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(max_length=50, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_options = models.CharField(max_length=50, null=False)
    payment_options = models.CharField(choices=PAYMENT_OPTIONS, max_length=50, null=True)
    payment_mode = models.CharField(choices=PAYMENT_MODE, null=True, max_length=50)
    any_other_comment =models.TextField(null=True)

    class meta:
        ordering =("name",)

class ServiceProvider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='serviceprovider')
    nin = models.CharField(_('National Identity Number (NIN)'),max_length=50, null=True, blank=False)
    service_provider_location = models.CharField(null=True, max_length=50)
    list_of_services_if_more_than_one = models.CharField(blank=True, max_length=50)
    service_type = models.CharField(max_length=50, null=True)
    phone_1 = PhoneNumberField(_('Phone number 1'), blank=False, null=True)
    phone_2 = PhoneNumberField(_('Phone number 2'), blank=True, null=True)
    is_the_service_available = models.BooleanField(choices=YES_OR_NO, null=True)
    service_location = models.CharField(max_length=100, null=True)
    is_the_service_at_a_fee = models.BooleanField(choices=YES_OR_NO, null=True)
    category = models.CharField(choices=SERVICE_CATEGORY,null=True,max_length=50)

    status = models.CharField(choices=STATUS, default='in_active', max_length=20,null=False)
    # handle approving of a farmer
    approver = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name="unffe_agent_service_provider",null=True,blank=True)
    approved_date = models.DateTimeField(blank=True, null=True)
    # location
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE,null=True)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE, null=True)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE, null=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)


    class meta:
        ordering =("service_type")

class Service(models.Model):
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, null=True)
    category = models.CharField(choices=SERVICE_CATEGORY,null=True, max_length=50)
    service_name = models.CharField(max_length=200, null=True)
    service_type = models.CharField(max_length=50, null=True)
    size =  models.FloatField(max_length=50, null=True)
    terms_and_conditions = models.BooleanField(default=True)
    availability_date = models.DateField(blank=True, null=True)
    availability_time = models.DateTimeField(auto_now_add=True, null=True) 
    picture = models.ImageField(null=True, blank=True)

    class meta:
        ordering =("service_type")

"""
location
contact details
availability date and time
terms and conditions

"""
class ContactDetails(models.Model):
    name = models.CharField(max_length=25, null=True)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = PhoneNumberField() # validators should be a list

   
    class Meta:
        ordering =("name",)

class Logistics(models.Model):
    name = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    source = models.CharField(max_length=50, null=True)
    destination = models.CharField(max_length=50, null=True)
    quantity = models.FloatField(max_length=50, null=True)
    time = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_mode = models.CharField(choices=PAYMENT_MODE, null=True, max_length=50)
    contact_details = models.ForeignKey(ContactDetails, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, default='True', max_length=20, null=False)
    inventory_status = models.CharField(choices=INVENTORY_STATUS, default=True, max_length=20,null=False)


    class Meta:
        ordering =("name",)

class Storage(models.Model):
    name = models.CharField(max_length=50, null=True)
    location = models.CharField(null=True, max_length=50)   
    size = models.FloatField(null=True)
    type = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True)
    available_services = models.CharField(max_length=50, blank=True)
    status = models.CharField(choices=STATUS, default='True', max_length=20, null=False)
    inventory_status = models.CharField(choices=INVENTORY_STATUS, default=True, max_length=20,null=False)



    class Meta:
        ordering =("name",)
        
class Packaging(models.Model):
    name = models.CharField(max_length=50, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.CharField(null=True, max_length=50) 
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    status = models.CharField(choices=STATUS, default='True', max_length=20, null=False)
    rent = models.CharField(max_length=25, null=True)

    class Meta:
        ordering =("name",)

class Medical(models.Model):
    name = models.CharField(max_length=50, null=True)
    enterprise = models.ForeignKey(to='farm.Enterprise',related_name='medical',on_delete=models.CASCADE)
    location = models.CharField(null=True, max_length=50) 
    status = models.CharField(choices=STATUS, default='True', max_length=20, null=False)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =("name",)


class SoilScience(models.Model):
    name = models.CharField(max_length=50, null=True)
    location = models.CharField(null=True, max_length=50) 
    operation_mode = models.CharField(max_length=50, null=True)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default='True', max_length=20, null=False)

    class Meta:
        ordering =("name",)

