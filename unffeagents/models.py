from django.db import models
from django.contrib.auth.models import User, Group
from openmarket.models import Product
from common.models import Region
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext as _
from common .models import (District,County,Region)
from common .models import TimeStampedModel


# Create your models here.
class AgentProfile(models.Model):
    SPECIFIC_ROLE = (
        (None, "--please select--"),
        ('account manager', 'Account Manager'),
        ('market manager', 'Market Manager'),
        ('call centre agent', 'Call Centre Agent'),
        ('notifications and alerts', 'Notifications and Alerts'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agents')
    contact = PhoneNumberField(blank=False)
    # agent address
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    specific_role = models.CharField(max_length = 50, choices=SPECIFIC_ROLE)

    def __str__(self):
        return self.specific_role


class Market(models.Model):
    market_name = models.CharField(max_length=100, blank = False)
    lat = models.FloatField(_('Latitude'), blank=True, null=True)
    lon = models.FloatField(_('Longitude'), blank=True, null=True)
    market_description = models.TextField(max_length=600, blank=False)

    def __str__(self):
        return self.market_name


class MarketPrice(TimeStampedModel, models.Model):
    market = models.ForeignKey(Market, blank = False, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='unffeagent')
    product = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE) # let it be product per price
    unit_of_measure = models.CharField(blank=False, max_length=100) # unit of measure like kilogram
    start_price = models.DecimalField(decimal_places=2, max_digits=20, blank=False)
    end_price = models.DecimalField(decimal_places=2, max_digits=20, blank=False)

    def __str__(self):
        return self.market


class Notice(TimeStampedModel, models.Model):
    CATEGORY = (
        (None, "--please select--"),
        ('weather', 'Weather'),
        ('inputs', 'Inputs'),
        ('market', 'Market'),
        ('pests and diseases', 'Pests and Diseases'),
        ('policies', 'Policies'),
    )

    notice_title = models.CharField(max_length=100, blank = False, null=False)
    category = models.CharField(choices=CATEGORY, blank=False, max_length=50)
    display_up_to = models.DateTimeField(blank = False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    target_audience = models.ManyToManyField(Group, related_name='target_groups')
    region = models.ManyToManyField(Region, related_name='target_regions')
    description = models.TextField(max_length=300, blank=False)
    upload = models.FileField(null=True)

    def __str__(self):
        return self.notice_title
