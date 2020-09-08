from django.db import models
from Auth.models import User
from common.models import(Region, District, County, SubCounty, Parish, Village)
from common.choices import(GENDER_CHOICES, MARITAL_STATUSES)
from django.core.validators import RegexValidator
# Create your models here.
class Product(models.Model):
     id = models.CharField(max_length=50, null=True, blank=True)
     name = models.CharField(max_length=50, null=True)
     enterprise = models.ForeignKey(Enterprise,related_name='products',on_delete=models.CASCADE)
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
    major_products = models.ManyToManyField(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-name',)
    def __str__(self):
        return self.name

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')

    class meta:
        ordering =("name",)

class SellerPost(models.Model):
    name = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(null=True)
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
    quantity = models.CharField(null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_options = models.CharField(null=False)
    payment_options = models.CharField(max_length=50, null=True)
    payment_mode = models.CharField(null=True, max_length=50)
    Any_other_comment =models.TextField(null=True)

    class meta:
        ordering =("name",)

class ServiceProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='serviceprovider')
    location = models.CharField(null=True, max_length=50)
    list_of_service = models.CharField(blank=True, max_length=50)
