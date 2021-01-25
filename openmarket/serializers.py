from rest_framework import serializers
from .models import (Product,
                     Seller,
                     SellerPost,
                     BuyerPost,
                     ServiceProvider,
                     Service,
                     ContactDetails,
                     Logistics,
                     SoilScience,Category,ProductCategory)
from django.contrib.auth.models import User
from farm.serializers import EnterpriseSerializer
from farm.models import Enterprise
from common.serializers import UserSerializer
from common.customSerializers import GeometryPointFieldSerializerFields


class ProductSerializer(serializers.ModelSerializer):
   
   # market = serializers.SerializerMethodField(method_name='get_market',source='market')

    class Meta:
        model = Product
        fields = '__all__'

 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =('id','cat_name')


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields ='__all__'



class SellerSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField(method_name='get_user_full_name',source='user')
    approver = serializers.SlugRelatedField(many=False,read_only=True, slug_field='first_name')
    major_products = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    seller_type = serializers.CharField(source='get_seller_type_display')

    class Meta:
        model = Seller
        fields = ('user','full_name','business_address', 'business_number', 'seller_type',
          'major_products', 'status', 'approver','approved_date')

    def get_user_full_name(self, obj):
        return '{} {}'.format(obj.user.first_name, obj.user.last_name)


class PostSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude =['status','approver','approved_date','user']


class SellerApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields =('status','approver','approved_date')



class SellerPostSerializer(serializers.ModelSerializer):
    payment_options = serializers.CharField(source='get_payment_options_display')
    payment_mode = serializers.CharField(source='get_payment_mode_display')
    product = serializers.SerializerMethodField(method_name='get_product',source='product')
    seller = serializers.SerializerMethodField(method_name='get_seller',source='seller')
    market = serializers.SerializerMethodField(method_name='get_market',source='product')

    class Meta:
        model = SellerPost
        fields = ('id','seller', 'product','market', 'quantity', 'price_offer', 'delivery_option','payment_options', 'payment_mode','product_description','product_image_1','product_image_2')

    def get_product(self, obj):
        try:
            return '{}'.format(obj.product.product.name)
        except:
            return None
    def get_seller(self, obj):
        try:
            return '{} {}'.format(obj.seller.user.first_name, obj.seller.user.last_name)
        except:
            return None
    def get_market(self, obj):
        try:
            return '{}'.format(obj.product.market.market_name)
        except:
            return None

class PostSellerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerPost
        exclude =['seller']



class BuyerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyerPost
        fields = ('name', 'current_location', 'product', 'total_cost', 'delivery_options', 'payment_options',
         'payment_mode', 'any_other_comment')

class ServiceProviderSerializer(serializers.ModelSerializer):
    #sector = serializers.PrimaryKeyRelatedField(many=True, queryset=Sector.objects.all())
    #sector = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
   # user = UserSerializer()
    category = serializers.SlugRelatedField(many=True,read_only=True, slug_field='cat_name')
    user = serializers.SerializerMethodField(method_name='get_user_full_name')
    
    class Meta:
        model = ServiceProvider
        fields = ('user_id','user',  'nin','service_provider_location','category', 'is_the_service_available', 'is_the_service_at_a_fee','status', 'approver',
         'approved_date','gender'
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


class PostServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        exclude=['user']

class ServiceProviderApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields =('status','approver','approved_date')


class ServiceRegistrationSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user_full_name')
    full_name = serializers.SerializerMethodField(method_name='get_user_full_name',source='user')
    #category = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    category = serializers.SlugRelatedField(many=False,read_only=True, slug_field='cat_name')
    location = GeometryPointFieldSerializerFields()


    class Meta:
        model = Service
        fields = ('user_id','user', 'service_name', 'size','category', 'availability_date', 'terms_and_conditions', 'availability_time', 'picture','description',
        'available_services','rent','name_of_storage_center','location_of_storage_center','certification_status',
        'vehicle_type','vehicle_capacity','location','others','full_name')

    def get_user_full_name(self, obj):
        return '{} {}'.format(obj.user.first_name, obj.user.last_name)


class PostServiceRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        exclude=['user']

class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = ('name', 'phone_number')


class LogisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logistics
        fields = ('name', 'source', 'destination', 'quantity', 'time', 'product', 'payment_mode',
        'contact_details')

class SoilScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilScience
        fields = ('name', 'location', 'status', 'operation_mode', 'time')
