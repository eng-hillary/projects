from rest_framework import serializers
from .models import (Sector, Enterprise, Farm, FarmFacility, Produce, FarmProduce, 
                    FinancialRecord, PestAndDisease, FarmRecord)


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['name', 'size']

class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ('name', 'sector', 'description')


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ('name', 'enterprise', 'farmer', 'latitude', 'longitude', 'initial_capital',
        'expexted_profit', 'start_date', 'animal_seed_density', 'image', 'status', 'general_remarks')


class FarmFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmFacility
        fields = ('name', 'farm', 'description', 'image')


class ProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produce
        fields = ('name', 'description', 'quantity')


class FarmProduceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmProduce
        fields = ('farm', 'produce', 'quantity', 'description', 'production_date', 'taken_by', 'reported_by')
