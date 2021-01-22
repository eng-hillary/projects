from rest_framework import serializers
from .models import (AgentProfile, Market, MarketPrice, Notice,Call,CallRsponse)
from django.contrib.auth.models import User
from openmarket.models import ProductOrdering

class ProductOrderingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrdering
        fields = ('id','product','quantity','delivery_date', 'delivery_address', 'payment_mode', 'payment_method', 'Additional_notes')


class AgentProfileSerializer(serializers.ModelSerializer):
    user_names = serializers.SerializerMethodField(method_name='get_user_full_name', read_only=True)
    region = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    user = serializers.SlugRelatedField(many=False,read_only=True, slug_field='username')
    district = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    class Meta:
        model = AgentProfile
        fields = ['id','user', 'contact', 'region', 'district', 'specific_role','user_names']

    def get_user_full_name(self, obj):
        return '{} {}'.format(obj.user.first_name, obj.user.last_name)

class PostAgentProfileSerializer(serializers.ModelSerializer):

  
    class Meta:
        model = AgentProfile
        exclude=['user']
        

class MarketSerializer(serializers.ModelSerializer):
    lat = serializers.SerializerMethodField(method_name='get_lat',source='location')
    lon = serializers.SerializerMethodField(method_name='get_lon',source='location')
    location = serializers.CharField(source='compute_location')
    class Meta:
        model = Market
        fields = ['id','market_name', 'lon', 'lat', 'market_description','location']
    

    def get_lat(self,obj):
        try:
            return '{}'.format(obj.location.y)
        except:
            pass
    def get_lon(self,obj):
        try:
            return '{}'.format(obj.location.x)
        except:
            pass


class MarketPriceSerializer(serializers.ModelSerializer):
    market = serializers.SlugRelatedField(many=False,read_only=True, slug_field='market_name')
    product = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    posted_by = serializers.SerializerMethodField(method_name='get_agent_name',source='user')

    class Meta:
        model = MarketPrice
        fields = ['id','market', 'posted_by', 'product', 'unit_of_measure', 'max_price', 'min_price','created']

    def get_agent_name(self, obj):
        try:
            return '{} {}'.format(obj.user.first_name, obj.user.last_name)
        except:
            return None

class NoticeSerializer(serializers.ModelSerializer):
    sector = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    district = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    region = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    county = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    sub_county = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    parish = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    target_audience = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    village = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    display_up_to = serializers.DateTimeField()
  
    class Meta:
        model = Notice
        fields ='__all__'


class CallSerializer(serializers.ModelSerializer):
    call_date = serializers.DateTimeField()
    responses = serializers.StringRelatedField(many=False)

    class Meta:
        model = Call
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    called_from = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    type_of_question = serializers.CharField(source='get_type_of_question_display')
    agent = serializers.SerializerMethodField(method_name='get_agent_name',source='agent')
    class Meta:
        model = CallRsponse
        fields = '__all__'
    

    def get_agent_name(self, obj):
        try:
            return '{} {}'.format(obj.agent.first_name, obj.agent.last_name)
        except:
            return None