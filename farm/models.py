from django.db import models
from django.utils.translation import ugettext as _
from common .models import(TimeStampedModel)
from django.contrib.auth.models import User
from common .choices import (TRANSACTION_TYPE, PAYMENT_MODE,YES_OR_NO,QUERIES)
from geopy.geocoders import Nominatim
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _
# Create your models here.


class Sector(TimeStampedModel, models.Model):
    SECTOR_SIZE =(
        (None, '--please select--'),
        ('small', 'Small'),
        ('large', 'Large')
    )
    name = models.CharField(max_length=50)
    size = models.CharField(choices=SECTOR_SIZE, null=False, max_length=20)

    def __str__(self):
        return self.name



class Farm(TimeStampedModel, models.Model):
    FARM_STATUS = (
        (None, '--please select--'),
        ('active', 'Active'),
        ('closed', 'Closed')
     )
    farm_name = models.CharField(max_length=100, null=False, blank=False)
    farmer = models.ForeignKey('farmer.FarmerProfile', on_delete=models.CASCADE, related_name='farms')
    lat = models.FloatField(_('Latitude'), blank=True, null=True, help_text="Latitude of your location")
    lon = models.FloatField(_('Longitude'), blank=True, null=True,help_text="Longitude of your location")
    start_date = models.DateField(blank=False, null=False)
    close_date = models.DateField(blank=True, null=True)
    image = models.ImageField(null=True, blank=False)
    status = models.CharField(_('Farm Status'), default='active', max_length=20, choices=FARM_STATUS)
    general_remarks = models.TextField(null=True, blank=True)
    availability_of_services = models.BooleanField(_('Have access to Services ?.'), choices=YES_OR_NO, null=False, blank=False, default=True)
    availability_of_water = models.BooleanField(_('Does a the farm have a water source ?.'), choices=YES_OR_NO, null=False, blank=False, default=True)
    land_occupied = models.FloatField( _('Amount of land occupied(acres)'), blank=False, null=True)
    available_land = models.FloatField( _('Size of land Available'), blank=True, null=True)

    def __str__(self):
        return self.farm_name

    @property
    def compute_location(self):
        geolocator = Nominatim(user_agent="ICT4Farmers", timeout=10)
        lat = str(self.lat)
        lon = str(self.lon)
       
        try:

            location = geolocator.reverse(lat + "," + lon)
            return '{}'.format(location)
        except:
            location = str(self.lat) + "," + str(self.lon)
            return 'slow network, loading location ...'


class EnterpriseType(TimeStampedModel, models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True)
  
    def __str__(self):
        return self.name



class Enterprise(TimeStampedModel, models.Model):
    Enterprise_STATUS = (
        (None, '--please select--'),
        ('open', 'Open'),
        ('closed', 'Closed')
     )
    name = models.CharField(_('Enterprise Name'), max_length=50, null=False, blank=False)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True, related_name='enterprises')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True, blank=False)
    enterprise_type = models.CharField(blank=False, null=True, max_length=200)
    animal_seed_density = models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of animals/seedling per enterprise in a particular period of time.')
    capital_invested = models.DecimalField(decimal_places=2, max_digits=1000, null=True)
    return_on_investment = models.DecimalField(_('Expected Return on Investment'), decimal_places=2, max_digits=1000, null=True)
    from_period = models.DateField(blank=False, null=True)
    to_period = models.DateField(blank=False, null=True)
    land_occupied = models.FloatField( blank=False, null=True)
    start_date = models.DateField(_('Farm Start Date'), blank=False, null=True)
    close_date = models.DateField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=False)
    status = models.CharField(_('Enterprise Status'), default='active', max_length=20, choices=Enterprise_STATUS)


    def __str__(self):
        return self.name



class FarmFacility(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    farm = models.ForeignKey(Farm, on_delete=models.DO_NOTHING, related_name='facilities')
    description = models.TextField( blank=True, null=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

'''
These are farm products
'''
class Produce(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField( blank=True, null=True)
    quantity = models.DecimalField(decimal_places=2, max_digits=20, blank=False)

    def __str__(self):
        return self.name


class FarmProduce(TimeStampedModel, models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.DO_NOTHING, null=False, blank=False, related_name='farm_produces')
    produce = models.ForeignKey(Produce, on_delete=models.DO_NOTHING)
    quantity = models.FloatField(blank=False, null=False)
    description = models.TextField( blank=True, null=True)
    production_date = models.DateField()
    taken_by = models.CharField(max_length=100, null=True, blank=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.produce)


class FinancialRecord(TimeStampedModel, models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.DO_NOTHING, null=False, blank=False, related_name='farm_financial_record')
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, max_length=100, null=False)
    spent_on = models.CharField(_('Payment for'),max_length=200)
    transaction_to = models.CharField(_('Payment To/From'),max_length=100)
    amount = models.FloatField(_('Amount paid'),blank=False, null=False)
    quantity = models.FloatField()
    means_of_payment = models.CharField(max_length=20, blank=False, null=False, choices=PAYMENT_MODE)
    transaction_date = models.DateField(auto_now=True)
    description = models.TextField( blank=True, null=True)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.spent_on


class PestAndDisease(TimeStampedModel, models.Model):
    query_category = models.CharField(choices=QUERIES, max_length=25, null=True, blank=False)
    farm = models.ForeignKey(Farm, on_delete=models.DO_NOTHING, null=False, blank=False, related_name='farm_pests_and_diseases')
    description = models.TextField( blank=True, null=True)
    date_discovered = models.DateField()
    action_taken = models.TextField( blank=False, null=True)
    image = models.ImageField(null=True, blank=False)
    reporting_date = models.DateField(auto_now=True)
    solution = models.TextField( blank=True, null=True)


    def __str__(self):
        return self.description
class RecordType(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name


class FarmRecord(TimeStampedModel, models.Model):

    enterprise = models.ForeignKey(Enterprise, on_delete=models.DO_NOTHING, null=True, blank=False, related_name='farm_records')
    record_type = models.ForeignKey(RecordType,null=True, blank=True, on_delete=models.DO_NOTHING)
    name = models.CharField(_('Activity'),max_length=200, null=False, blank=False)
    from_date = models.DateField()
    to_date = models.DateField()
    description = models.TextField( blank=True, null=True)
    # person responsible
    taken_by = models.CharField(_('Taken by'), blank=False, null=True, max_length=100)
    contact =  PhoneNumberField(_('Phone number'), blank=False, null=True)
    next_activity_date = models.DateField(null=True, blank=True)
    #reported_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
