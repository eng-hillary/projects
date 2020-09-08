from django.db import models
from Auth.models import User

# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller')
    date_of_birth = models.DateField(max_length=8)
    
