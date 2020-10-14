from rest_framework import serializers
from .models import (Product, 
                     Seller, 
                     Buyer, 
                     SellerPost, 
                     BuyerPost, 
                     ServiceProvider, 
                     Service,
                     ContactDetails, 
                     Logistics, 
                     SoilScience)
from django.contrib.auth.models import User
from farm.serializers import EnterpriseSerializer
from farm.models import Enterprise
from common.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    enterprise = serializers.PrimaryKeyRelatedField(many=False, queryset=Enterprise.objects.all())
    enterprise = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'enterprise', 'slug', 'image', 'description', 'price', 'available',
         'date_created', 'date_updated')

class SellerSerializer(serializers.ModelSerializer):
    enterprise = serializers.PrimaryKeyRelatedField(many=False, queryset=Enterprise.objects.all())
    enterprise = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    major_products = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    user = serializers.SlugRelatedField(many=False,read_only=True, slug_field='username')
    region = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    district = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    county = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    sub_county = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    parish = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    village = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    approver = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    

   # enterprise = EnterpriseSerializer()
    class Meta:
        model = Seller
        fields = ('id','user', 'business_number', 'business_location', 'seller_type', 'date_of_birth','region',
         'district', 'county', 'sub_county', 'parish', 'village', 'gender','marital_status', 'enterprise',
          'major_products', 'status', 'approver','approved_date')


class SellerApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields =('status','approver','approved_date')


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ('user', 'created', 'modified')

class SellerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerPost
        fields = ('name', 'product', 'quantity', 'price_offer', 'delivery_option','payment_options', 'payment_mode')


class BuyerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerPost
        fields = ('name', 'current_location', 'product', 'total_cost', 'delivery_options', 'payment_options',
         'payment_mode', 'any_other_comment')

class ServiceProviderSerializer(serializers.ModelSerializer):
    #sector = serializers.PrimaryKeyRelatedField(many=True, queryset=Sector.objects.all())
    #sector = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
   # user = UserSerializer()
    user = serializers.SerializerMethodField(method_name='get_user_full_name')
    full_name = serializers.SerializerMethodField(method_name='get_user_full_name',source='user')
    region = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    district = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    county = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    sub_county = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    parish = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    village = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
   # group = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    #service_location = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name' )
   # credit_access = serializers.SerializerMethodField(method_name='conversion_bool',source='Credit access')

    class Meta:
        model = ServiceProvider
        fields = ('id','user', 'nin', 'region', 'district', 'county', 'full_name',
        'sub_county', 'region', 'parish', 'village','service_provider_location', 'list_of_services_if_more_than_one',
       'phone_1', 'phone_2', 'service_type', 'is_the_service_available', 'service_location', 'is_the_service_at_a_fee','status', 'approver', 'approved_date'
       )
    '''
    returns yes or no for boolean fields
    '''
    def conversion_bool(self, instance):
        if instance.is_the_service_available == True:
            return "Yes"
        else:
            return "No"


    def get_user_full_name(self, obj):
        return '{} {}'.format(obj.user.first_name, obj.user.last_name)


class ServiceProviderApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields =('status','approver','approved_date')


class ServiceRegistrationSerializer(serializers.ModelSerializer):
   # user = serializers.SerializerMethodField(method_name='get_user_full_name')
    user = serializers.SerializerMethodField(method_name='get_user_full_name')
    full_name = serializers.SerializerMethodField(method_name='get_user_full_name',source='user')
    #user = UserSerializer()
    #full_name = serializers.SerializerMethodField(method_name='get_user_full_name',source='username')
    #serializers.SerializerMethodField(method_name='get_user_full_name',source='user')

    class Meta:
        model = Service
        fields = ('user','category', 'service_name', 'service_type', 'size', 'availability_date', 'terms_and_conditions', 'availability_time', 'picture','description',
        'available_services','rent','name_of_storage_center','location_of_storage_center','certification_status',
        'vehicle_type','vehicle_capacity','lat','lon','others','full_name')
   
    def get_user_full_name(self, obj):
        return '{} {}'.format(obj.user.first_name, obj.user.last_name)


class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = ('name', 'phone_number')


class LogisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logistics
        fields = ('name', 'source', 'destination', 'quantity', 'time', 'product', 'payment_mode', 
        'contact_details', 'image', 'description', 'status', 'inventory_status')

class SoilScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilScience
        fields = ('name', 'location', 'status', 'operation_mode', 'time')