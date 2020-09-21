from rest_framework import serializers
from .models import (Product, 
                     Seller, 
                     Buyer, 
                     SellerPost, 
                     BuyerPost, 
                     ServiceProvider, 
                     ServiceRegistration, 
                     ContactDetails, 
                     Logistics, 
                     Storage, 
                     Packaging, 
                     Medical, 
                     SoilScience)
from django.contrib.auth.models import User
from farm.serializers import EnterpriseSerializer
from farm.models import Enterprise

class ProductSerializer(serializers.ModelSerializer):
    enterprise = serializers.PrimaryKeyRelatedField(many=False, queryset=Enterprise.objects.all())
    
    class Meta:
        model = Product
        fields = ('name', 'enterprise', 'slug', 'image', 'description', 'price', 'available',
         'date_created', 'date_updated')

class SellerSerializer(serializers.ModelSerializer):
    enterprise = serializers.PrimaryKeyRelatedField(many=True, queryset=Enterprise.objects.all())
    #enterprise = EnterpriseSerializer()
    class Meta:
        model = Seller
        fields = ('user', 'business_number', 'business_location', 'seller_type', 'date_of_birth','region',
         'district', 'county', 'sub_county', 'parish', 'village', 'gender','marital_status', 'enterprise',
          'major_products', 'status', 'approver', 'approved_date')

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
    class Meta:
        model = ServiceProvider
        fields = ('user', 'location', 'list_of_service', 'service_type')

class ServiceRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRegistration
        fields = ('service_id', 'type')
      

class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = ('name', 'phone_number')


class LogisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logistics
        fields = ('name', 'source', 'destination', 'quantity', 'time', 'product', 'payment_mode', 
        'contact_details', 'image', 'description', 'status', 'inventory_status')


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ('name', 'location', 'size', 'type', 'description', 'available_services', 'status',
         'inventory_status')


class PackagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packaging
        fields = ('name', 'product', 'location', 'image', 'status', 'rent')



class MedicalSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(many=True, read_only=True)
    class Meta:
        model = Medical
        fields = ('name', 'enterprise', 'location', 'status', 'time')



class SoilScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilScience
        fields = ('name', 'location', 'status', 'operation_mode', 'time')