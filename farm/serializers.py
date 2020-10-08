from rest_framework import serializers
from .models import (Sector, Enterprise, Farm, FarmFacility, Produce, FarmProduce, 
                    FinancialRecord, PestAndDisease, FarmRecord, EnterpriseType)
from farmer .serializers import FarmerProfileSerializer

from geopy.geocoders import Nominatim



class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id','name', 'size']




class FarmSerializer(serializers.ModelSerializer):
    #sector = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')

    location = serializers.CharField(source='compute_location')
    farmer = FarmerProfileSerializer()
    status = serializers.CharField(source='get_status_display')
    availability_of_services = serializers.SerializerMethodField(method_name='conversion_bool',source='availability_of_services')
    availability_of_water = serializers.SerializerMethodField(method_name='water_conv_bool',source='availability_of_water')

    class Meta:
        model = Farm
        fields = ('id', 'farm_name', 'farmer', 'lat', 'lon','location',
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

class EnterpriseTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EnterpriseType
        fields = '__all__'



class EnterpriseSerializer(serializers.ModelSerializer):
    farm = FarmSerializer()
    sector = SectorSerializer()
    enterprise_type = EnterpriseTypeSerializer()
    class Meta:
        model = Enterprise
        fields = '__all__'


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

# serialiser for the maps 
class FarmMapSerializer(serializers.ModelSerializer):

    farmer = serializers.SerializerMethodField(method_name='get_user_full_name',source='farmer__user')
    district = serializers.SerializerMethodField(method_name='get_district',source='farmer')
    class Meta:
        model = Farm
        fields = ('district','farm_name','farmer',  'lat', 'lon','land_occupied')



    def get_user_full_name(self, obj):
        return '{} {}'.format(obj.farmer.user.first_name, obj.farmer.user.last_name)

    def get_district(self, obj):
        return '{}'.format(obj.farmer.district.name)