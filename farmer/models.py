from django.db import models
from django.contrib.auth.models import User
from common.models import(Region, District, County, SubCounty, Parish, Village, TimeStampedModel)
from common.choices import(GENDER_CHOICES, MARITAL_STATUSES, LAND_TYPES, PRODUCTION_SCALE, YES_OR_NO)
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _
from farm .models import Sector

# Create your models here.

class Group(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=False)
    logo = models.ImageField()
    address = models.CharField(max_length=200, blank=False, null=False)
    contact_person = models.CharField(max_length=100)
    contact_person_email = models.EmailField(null=True)
    contact_person_phone = PhoneNumberField(blank=False, null=False)

    def __str__(self):
        return self.name


class FarmerProfile(TimeStampedModel, models.Model):
    STATUS = (
        ('active', 'Active'),
        ('in_active', 'In-Active'),
        ('rejected', 'Rejected')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer')
    date_of_birth = models.DateField()
    nin = models.CharField(max_length=50, null=False, blank=False)
    sector = models.ManyToManyField(Sector, related_name='farmer_sectors')
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
    type_of_land = models.CharField(choices=LAND_TYPES, max_length=20)
    production_scale = models.CharField(choices=PRODUCTION_SCALE, max_length=20)
    number_of_dependants = models.PositiveIntegerField()
    # initial capital moved to farm
    #initial_total_capital = models.DecimalField(decimal_places=2, max_digits=20, blank=False)
<<<<<<< HEAD
    
=======
    credit_access = models.BooleanField(_('Have access to credit ?.'), choices=YES_OR_NO, null=False, blank=False)
>>>>>>> 4136e3c639cef14ee456535c2b845b10dce68e07
    experience = models.FloatField(_('Experience in years'),null=False, blank=False)
    status = models.CharField(default='in_active', max_length=20,null=False)
    general_remarks = models.TextField(null=True, blank=True)
    # handle approving of a farmer
    approver = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name="unffe_agent",null=True,blank=True)
    approved_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.user)
