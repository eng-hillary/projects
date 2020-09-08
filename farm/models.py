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
    description = models.TextField(null=True, blank=True)
    initial_capital = models.DecimalField(decimal_places=2, max_digits=4)
    expected_profit = models.DecimalField(decimal_places=2, max_digits=4)

    def __str__(self):
        return self.name



class Farm(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    

