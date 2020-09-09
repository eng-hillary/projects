from rest_framework import serializers
from .models import Product, Seller, Buyer, SellerPost, BuyerPost, ServiceProvider, ServiceRegistration, ContactDetails, Logistics, Storage, Packaging, Medical, SoilScience
from django.contrib.auth.models import User
from farm.serializers import EnterpriseSerializer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    enterprise = EnterpriseSerializer()
    class Meta:
        model = Product
        fields = ('name', 'enterprise', 'slug', 'image', 'description', 'price', 'available',
         'date_created', 'date_updated')

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    enterprise = EnterpriseSerializer()
    class Meta:
        model = Seller
        fields = ('user', 'business_number', 'business_location', 'seller_type', 'date_of_birth',
         'price', 'region', 'district', 'county', 'sub_county', 'parish', 'village', 'gender', 
         'marital_status', 'enterprise', 'major_products')

class BuyerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buyer
        fields = ('user')

class SellerPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SellerPost
        fields = ('name', 'product', 'quantity', 'price_offer', 'delivery_options', 'payment_mode')


class BuyerPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BuyerPost
        fields = ('name', 'current_location', 'product', 'total_cost', 'delivery_options', 'payment_options',
         'payment_mode', 'any_other_comments')


class ServiceProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ('user', 'location', 'list_of_service', 'service_type')

class ServiceRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceRegistration
        fields = ('service_id', 'type')
      

class ContactDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactDetails
        fields = ('name', 'phone_number')


class LogisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Logistics
        fields = ('name', 'source', 'destination', 'quantity', 'time', 'product', 'payment_mode', 
        'contact_details', 'image', 'description', 'status', 'inventory_status')


class StorageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storage
        fields = ('name', 'location', 'size', 'type', 'description', 'available_services', 'status',
         'inventory_status')


class PackagingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Packaging
        fields = ('name', 'product', 'location', 'image', 'status', 'rent')



class MedicalSerializer(serializers.HyperlinkedModelSerializer):
    enterprise = EnterpriseSerializer()
    class Meta:
        model = Medical
        fields = ('name', 'enterprise', 'location', 'status', 'time')



class SoilScienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoilScience
        fields = ('name', 'location', 'status', 'operation_mode', 'time')