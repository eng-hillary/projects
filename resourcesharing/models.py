from django.db import models
from django.contrib.auth.models import User
from common.choices import(RESOURCE_CATEGORY)
from farmer.models import FarmerProfile

# Create your models here.
class Resource(models.Model):
    RESOURCE_STATUS = (
         (None, "---please select---"),
        ('available', 'Available'),
        ('not available', 'Not Available')
    )
    resource_name = models.CharField(max_length=200, blank = False)
    resource_provider_details = models.CharField(max_length = 400, blank = False)
    resource_provider_contact = PhoneNumberField(blank = False)
    resource_category = models.ChoiceField(RESOURCE_CATEGORY)
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    latitude = models.FloatField(min_value=-90, max_value=90)
    longitude = models.FloatField(min_value=-180, max_value=180)
    termsandconditions = models.TextField(max_length=400, blank = False)
    resource_status = models.CharField(max_length=20, choices=RESOURCE_STATUS)
    availability_date_and_time = models.datetime(blank = false) #this should be a dynamic field
    price = models.DecimalField(blank = False)
    phone = models.PhoneNumberField(blank = False)

    def __str__(self):
        return self.resource_name

class ResourceSharing(models.Model):
    resource = models.ForeignKey(Resource, on_delete = models.CASCADE)
    date_required = models.datetime(blank = True)


    def __str__(self):
        return self.resource

class ResourceBooking(models.Model):
    resource = models.ForeignKey(Resource, on_delete = models.CASCADE)
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    date_needed = models.datetime(blank = True)
    duration = models.IntegerField(blank = False)
    resource_user_details = models. CharField(max_length=100, blank=False)


    def __str__(self):
        return self.resource
