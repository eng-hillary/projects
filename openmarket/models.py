from django.db import models
from django.contrib.auth.models import User
from common.models import(Region, District, County, SubCounty, Parish, Village)
from common.choices import(GENDER_CHOICES, MARITAL_STATUSES)
from django.core.validators import RegexValidator
from farm.models import Enterprise
# Create your models here.
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

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    business_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    business_location = models.CharField(null=True, max_length=50)
    seller_type = models.CharField(max_length=15, null=False)
    date_of_birth = models.DateField(max_length=8)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15)
    marital_status = models.CharField(choices=MARITAL_STATUSES, max_length=15, null=False, blank=False)
    enterprise = models.TextField(null= True)
    major_products = models.ManyToManyField(Product, related_name='seller')

    class Meta:
        ordering = ('seller_type',)
    def __str__(self):
        return self.seller_type

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')

    class meta:
        ordering =("name",)

class SellerPost(models.Model):
    name = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(max_length=50, null=True)
    price_offer = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_option = models.CharField(max_length=50)
    payment_options = models.CharField(max_length=50, null=True)
    payment_mode = models.CharField(null=True, max_length=50)

    class Meta:
        ordering = ('-name',)

class BuyerPost(models.Model):
    name = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    current_location = models.CharField(max_length=50)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(max_length=50, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_options = models.CharField(max_length=50, null=False)
    payment_options = models.CharField(max_length=50, null=True)
    payment_mode = models.CharField(null=True, max_length=50)
    Any_other_comment =models.TextField(null=True)

    class meta:
        ordering =("name",)

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='serviceprovider')
    location = models.CharField(null=True, max_length=50)
    list_of_service = models.CharField(blank=True, max_length=50)
    service_type = models.CharField(max_length=50, null=True)

    class meta:
        ordering =("-name",)

class ServiceRegistration(models.Model):
    service_id = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50)

    class Meta:
        ordering =("type",)

class ContactDetails(models.Model):
    name = models.CharField(max_length=25, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

class Logistics(models.Model):
    name = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    source = models.CharField(max_length=50, null=True)
    destination = models.CharField(max_length=50, null=True)
    quantity = models.FloatField(max_length=50, null=True)
    Time = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_mode = models.CharField(null=True, max_length=50)
    contact_details = models.ForeignKey(ContactDetails, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=True)
    inventory_status = models.BooleanField(default=True)


    class Meta:
        ordering =("name",)

class Storage(models.Model):
    name = models.CharField(max_length=50, null=True)
    location = models.CharField(null=True, max_length=50)   
    size = models.FloatField(null=True)
    type = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True)
    available_services = models.CharField(max_length=50, blank=True)
    status = models.BooleanField(default=True)
    inventory_status = models.BooleanField(default=True)

    class Meta:
        ordering =("name",)

class Packaging(models.Model):
    name = models.CharField(max_length=50, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.CharField(null=True, max_length=50) 
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    status = models.BooleanField(default=True)
    rent = models.CharField(max_length=25, null=True)

    class Meta:
        ordering =("name",)

class Medical(models.Model):
    name = models.CharField(max_length=50, null=True)
    enterprise = models.ForeignKey(to='farm.Enterprise',related_name='medical',on_delete=models.CASCADE)
    location = models.CharField(null=True, max_length=50) 
    status = models.BooleanField(default=True)
    Time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =("name",)

class SoilScience(models.Model):
    name = models.CharField(max_length=50, null=True)
    location = models.CharField(null=True, max_length=50) 
    status = models.BooleanField(default=True)
    operation_mode = models.CharField(max_length=50, null=True)
    Time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =("name",)
