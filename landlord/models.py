from django.db import models
from customer.models import*
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.

class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True,blank=True)
    fname = models.CharField(max_length=20,null=True)
    lname = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=200, null=True)
    contact = models.CharField(max_length=20,null=True)
    picture = models.ImageField(upload_to='images',null=True,blank=True,default='default.png')

    def __str__(self):
       return f"{self.fname} {self.lname}"


class House(models.Model):
    CATEGORIES = (
                    ('flat','Flat'),
                    ('apartment','Apartment'),
                    ('boys quarter','Boys Quarter'),
                    
                 )
    STATUS = (
                ('vacant','Vacant'),
                ('booked','Booked'),
                ('occupied','Occupied'),
            )

    APPROVAL = (
        ('approved','Approved'),
        ('unapproved','Unapproved'),
        
    )
    owner = models.ForeignKey(Owner,null=True,on_delete=models.CASCADE,blank=True)
    category = models.CharField(choices=CATEGORIES, max_length=20,null=True)
    location = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    rooms = models.IntegerField(null=True,blank=True)
    picture = models.ImageField(upload_to='images',null=True,blank=True, default='home.png')
    description = models.TextField(max_length=200, blank=True,null=True)
    price = models.FloatField(max_length=10,null=True)
    status = models.CharField(choices=STATUS,max_length=20,null=True,default='vacant')
    approval = models.CharField(choices=APPROVAL,max_length=20,null=True,default='unapproved')


    def __str__(self):
        return f"{self.category} {self.price}"
    
