from django.db import models
from openmarket.models import Product
from common.models import Region


# Create your models here.
class AgentProfile(models.Model):
    SPECIFIC_ROLE = (
        (None, "--please select--"),
        ('account manager', 'Account Manager'),
        ('market manager', 'Market Manager'),
        ('call centre agent', 'Call Centre Agent'),
        ('notifications and alerts', 'Notifications and Alerts'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='unffeagent')
    contact = models.PhoneNumberField(blank=false)
    latitude = models.FloatField(min_value=-90, max_value=90)
    longitude = models.FloatField(min_value=-180, max_value=180)
    specific_role = models.ChoiceField(max_length = 100)

    def __str__(self):
        return self.specific_role

class Market(models.Model):
    market_name = models.CharField(max_length=100, blank = False)
    latitude = models.FloatField(min_value=-90, max_value=90)
    longitude = models.FloatField(min_value=-180, max_value=180)
    market_description = models.TextField(max_length=600, blank=False)

    def __str__(self):
        return self.market_name

class MarketPrice(models.Model):
    market = models.ForeignKey(Market, blank = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='unffeagent')
    product = models.ForeignKey(Product, blank=False)#Allow for adding of many products
    unit_of_measure = models.IntegerField(blank=False)
    start_price = models.DecimalField(blank = False)
    end_price = models.DecimalField(blank = False)

    def __str__(self):
        return self.market

class Notices(models.Model):
    CATEGORY = (
        (None, "--please select--"),
        ('weather', 'Weather'),
        ('inputs', 'Inputs'),
        ('market', 'Market'),
        ('pests and diseases', 'Pests and Diseases'),
        ('policies', 'Policies'),
    )

    notice_title = models.CharField(max_length=100, blank = False)
    category = models.ChoiceField(CATEGORY, blank=False)
    date = models.datetime(blank = False)
    by_who = models.CharField(max_length = 100, blank=False)
    target_audience = models. CharField(max_length = 100, blank=False)
    region = models.ForeignKey(Region, blank=False)
    description = models.TextField(max_length=300, blank=False)
    validity_period = models.IntegerField(blank=False)
    file = models.FileField(blank = False)

    def __str__(self):
        return self.notice_title
