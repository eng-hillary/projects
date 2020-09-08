from django.db import models
from django.contrib.auth.models import User
from common.models import(Region, District, County, SubCounty, Parish, Village)
from common.choices import(GENDER_CHOICES, MARITAL_STATUSES)
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=False)
    logo = models.ImageField()
    address = models.CharField(max_length=200, blank=False, null=False)
    contact_person = models.Charlocationield(max_length=100)
    contact_person_email = models.EmailField(null=True)
    contact_person_phone = PhoneNumberField(blank=False, null=False)

    def __str__(self):
        return self.name


class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer')
    date_of_birth = models.DateField()
    nin = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)
    parish = models.ForeignKey(Parish, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    level_of_education = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15)
    marital_status = models.CharField(choices=MARITAL_STATUSES, max_length=15, null=False, blank=False)
    land_owned = models.DecimalField(decimal_places=2, max_digits=20, blank=False)
    phone_1 = PhoneNumberField(blank = False)
    phone_2 = PhoneNumberField(blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, null=True, blank=True)


    

