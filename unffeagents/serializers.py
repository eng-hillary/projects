from rest_framework import serializers
from .models import (AgentProfile, Market, MarketPrice, Notice,Caller,CallRsponse)
from django.contrib.auth.models import User


class AgentProfileSerializer(serializers.ModelSerializer):
    region = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    user = serializers.SlugRelatedField(many=False,read_only=True, slug_field='username')
    district = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    class Meta:
        model = AgentProfile
        fields = ['user', 'contact', 'region', 'district', 'specific_role']


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['market_name', 'latitude', 'longitude', 'market_description']


class MarketPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketPrice
        fields = ['market', 'user', 'product', 'unit_of_measure', 'start_price', 'end_price']

class NoticeSerializer(serializers.ModelSerializer):
    target_audience = serializers.PrimaryKeyRelatedField(many=False, queryset=Notice.objects.all())
    region = serializers.PrimaryKeyRelatedField(many=False, queryset=Notice.objects.all())
    class Meta:
        model = Notice
        fields = ['notice_title', 'category', 'display_up_to', 'posted_by', 'target_audience', 'region',
        'description', 'upload']


class CallSerializer(serializers.ModelSerializer):
    call_date = serializers.DateTimeField()
    class Meta:
        model = Caller
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRsponse
        fields = '__all__'