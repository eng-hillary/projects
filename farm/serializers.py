from rest_framework import serializers
from .models import (Sector, Enterprise, Farm, FarmFacility, Produce, FarmProduce,Query, 

                    FinancialRecord, FarmRecord, EnterpriseType,FarmRecord,EnterpriseSelection,)

from farmer .serializers import FarmerProfileSerializer
from django.contrib.auth.models import User

from geopy.geocoders import Nominatim



class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['id','name', 'size']


class FarmSerializer(serializers.ModelSerializer):
    #sector = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')

    location = serializers.CharField(source='compute_location')
    farmer = serializers.SerializerMethodField(method_name='get_farmer_name',source='farmer')
    status = serializers.CharField(source='get_status_display')
    availability_of_services = serializers.SerializerMethodField(method_name='conversion_bool',source='availability_of_services')
    availability_of_water = serializers.SerializerMethodField(method_name='water_conv_bool',source='availability_of_water')

    class Meta:
        model = Farm
        fields = ('id', 'farm_name', 'farmer', 'lat', 'lon','location',
         'start_date','close_date',  'image','availability_of_services','availability_of_water','land_occupied','available_land', 'status', 'general_remarks')

    def get_farmer_name(self, obj):
        return '{} {}'.format(obj.farmer.user.first_name, obj.farmer.user.last_name)


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


class FarmRecordSerializer(serializers.ModelSerializer):
    record_type = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    enterprise = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    class Meta:
        model = FarmRecord
        fields = '__all__'


class FarmFinancilRecordSerializer(serializers.ModelSerializer):
    enterprise = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    transaction_type = serializers.CharField(source='get_transaction_type_display')
    means_of_payment = serializers.CharField(source='get_means_of_payment_display')

    class Meta:
        model = FinancialRecord
        fields = '__all__'


class EnterpriseTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EnterpriseType
        fields = '__all__'



class EnterpriseSerializer(serializers.ModelSerializer):
    farm = serializers.SlugRelatedField(many=False,read_only=True, slug_field='farm_name')
    sector = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    class Meta:
        model = Enterprise
        fields = '__all__'


class QuerySerializer(serializers.ModelSerializer):
    farm = FarmSerializer()
    class Meta:
        model = Query

        fields = ['id','query_category','farm', 'description', 'date_discovered',
        'action_taken', 'image', 'reporting_date', 'solution']


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
    region = serializers.SerializerMethodField(method_name='get_region',source='farmer')
    class Meta:
        model = Farm
        fields = ('id','region','district','farm_name','farmer',  'lat', 'lon','land_occupied')



    def get_user_full_name(self, obj):
        return '{} {}'.format(obj.farmer.user.first_name, obj.farmer.user.last_name)

    def get_district(self, obj):
        return '{}'.format(obj.farmer.district.name)

    
    def get_region(self, obj):
        return '{}'.format(obj.farmer.region.name)

class EnterpriseSelectionSerializer(serializers.ModelSerializer):
     user = serializers.SerializerMethodField(method_name='get_user_full_name')
     #full_name = serializers.SerializerMethodField(method_name='get_user_full_name',source='user')
     #user = serializers.SerializerMethodField(method_name='get_id')
     

     
     class Meta:
         model = EnterpriseSelection
         fields = ('own_piece_of_land','what_is_your_inspiration_for_considering_in_farming',
        'involved_in_anyother_farming_activity','scale','sector','full_time_devotion',
        'time_allocated_to_farming','interested_sector','capital','user')
    
     def get_user_full_name(self, obj):
         return '{} {}'.format(obj.user.first_name, obj.user.last_name)
    
     
    #  def get_id(self, obj):
    #      return '{}'.format(obj.user.id)
