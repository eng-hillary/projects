from django.db import models
from django.contrib.auth.models import User
from common.choices import(RESOURCE_CATEGORY, PAYMENT_MODE,PAYMENT_OPTIONS)
from farmer.models import FarmerProfile
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _


# Create your models here.
class Resource(models.Model):
    RESOURCE_STATUS = (
         (None, "---please select---"),
        ('available', 'Available'),
        ('not available', 'Not Available')
    )
    resource_name = models.CharField(max_length=200, blank = False)
    owner = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    contacts = PhoneNumberField(blank = False)
    resource_category = models.CharField(choices=RESOURCE_CATEGORY, max_length=25, null=False, blank=False)
    latitude = models.FloatField(_('Latitude'), blank=True, null=True)
    longitude = models.FloatField(_('Longitude'), blank=True, null=True)
    termsandconditions = models.TextField(max_length=400, blank = False)
    resource_status = models.CharField(max_length=20, choices=RESOURCE_STATUS)
    availability_date_and_time = models.DateTimeField(blank =False,null=True) #this should be a dynamic field
    price = models.DecimalField(decimal_places=2, max_digits=20, blank=False)

    def __str__(self):
        return self.resource_name


class ResourceSharing(models.Model):
    resource = models.ForeignKey(Resource, on_delete = models.CASCADE)
    date_taken = models.DateTimeField(blank = False, null=False)
    expected_return_date = models.DateTimeField(blank=False, null=False)
    # taken_by = models.ForeignKey(User)
    taken_by = models.CharField(max_length=100,null=False)
    phone_1 = PhoneNumberField(verbose_name='contact phone of person who took the resource')
    phone_2 = PhoneNumberField(verbose_name='contact phone of person who took the resource')

    def __str__(self):
        return self.resource


class ResourceBooking(models.Model):
    resource = models.ForeignKey(Resource, on_delete = models.CASCADE)
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    date_needed = models.DateTimeField(blank = True)
    payment_mode = models.CharField(choices=PAYMENT_MODE, null=True, blank=True, max_length=25)
    payment_method = models.CharField(choices=PAYMENT_OPTIONS, max_length=25,null=True, blank=True)

    def __str__(self):
        return self.resource
