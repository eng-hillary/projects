from django.db import models
from Auth.models import User
from common.models import(Region, District, County, SubCounty, Parish, Village)
from common.choices import(GENDER_CHOICES, MARITAL_STATUSES)
from django.core.validators import RegexValidator
# Create your models here.
class product(models.Model):
     id = models.CharField(max_length=50, null=True, blank=True)
     name = models.CharField(max_length=50, null=True)
     description = models.TextField(null=True)
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
    major_products = models.ManyToManyField(product, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-name',)
    def __str__(self):
        return self.name

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')

    class meta:
        ordering =("name",)

