from rest_framework import serializers
from .models import (Sector, Enterprise, Farm, FarmFacility, Produce, FarmProduce, 
                    FinancialRecord, PestAndDisease, FarmRecord)


class SectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sector
        fields = ['name', 'size']

class EnterpriseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enterprise
        fields = ('name', 'sector', 'description')