from rest_framework import serializers
from .models import (Sector, Enterprise, Farm, FarmFacility, Produce, FarmProduce, 
                    FinancialRecord, PestAndDisease, FarmRecord)


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id','name', 'size']


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ('name','animal_seed_density', 'sector','expected_profit', 'description')


class FarmSerializer(serializers.ModelSerializer):
    sector = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')

    class Meta:
        model = Farm
        fields = ('id', 'name', 'sector', 'farmer', 'latitude', 'longitude',
         'start_date','close_date',  'image','availability_of_services','availability_of_water','land_occupied', 'status', 'general_remarks')


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
