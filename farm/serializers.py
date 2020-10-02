from rest_framework import serializers
from .models import (Sector, Enterprise, Farm, FarmFacility, Produce, FarmProduce, 
                    FinancialRecord, PestAndDisease, FarmRecord)
from farmer .serializers import FarmerProfileSerializer

from geopy.geocoders import Nominatim



class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id','name', 'size']


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ('name','animal_seed_density', 'farm','expected_profit', 'description')


class FarmSerializer(serializers.ModelSerializer):
    #sector = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    location = serializers.SerializerMethodField(method_name='get_farm_location')
    farmer = FarmerProfileSerializer()
    status = serializers.CharField(source='get_status_display')
    availability_of_services = serializers.SerializerMethodField(method_name='conversion_bool',source='availability_of_services')
    availability_of_water = serializers.SerializerMethodField(method_name='water_conv_bool',source='availability_of_water')

    class Meta:
        model = Farm
        fields = ('id', 'name', 'farmer', 'latitude', 'longitude','location',
         'start_date','close_date',  'image','availability_of_services','availability_of_water','land_occupied','available_land', 'status', 'general_remarks')

    
    def conversion_bool(self, instance):
        if instance.availability_of_services == True:
            return "Yes"
        else:
            return "No"

    def water_conv_bool(self, instance):
        if instance.availability_of_water == True:
            return "Yes"
        else:
            return "No"

    
    def get_farm_location(self, obj):
        geolocator = Nominatim(user_agent="ICT4Farmers", timeout=10)
        lat = str(obj.latitude)
        lon = str(obj.longitude)
        print("52.509669"+"," + "13.376294")
       
        try:

            location = geolocator.reverse(lat + "," + lon)
            return '{}'.format(location)
        except:
            location = str(obj.latitude) + "," + str(obj.longitude)
            return 'slow network, loading location ...'

        # return '{}'.format(location)


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
