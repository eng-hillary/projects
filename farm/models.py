from django.db import models

# Create your models here.

class Sector(models.Model):
    SECTOR_SIZE =(
        (None, '--please select--'),
        ('small', 'Small'),
        ('large', 'Large')
    )
    name = models.CharField(max_length=50)
    size = models.CharField(choices=SECTOR_SIZE, null=False, max_length=20)
    
    def __str__(self):
        return self.name


class Enterprise(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class EnterpriseVariety(models.Model):
    name = models.CharField(max_length=100)
    

