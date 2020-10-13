from rest_framework import serializers
from .models import (Resource, ResourceSharing, ResourceBooking)


class ResourceSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(method_name='get_user_full_name',source='user')
    class Meta:
        model = Resource
        fields = ['id','resource_name', 'owner', 'Phone_number1', 'Phone_number2','resource_category', 'lat', 'lon',
        'terms_and_conditions', 'resource_status', 'available_from','available_to', 'price','image']

    def get_user_full_name(self, obj):
        return '{} {}'.format(obj.owner.user.first_name, obj.owner.user.last_name)


class ResourceSharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceSharing
        fields = ('resource', 'date_taken', 'expected_return_date', 'taken_by', 'phone_1', 'phone_2')


class ResourceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceBooking
        fields = ('resource', 'farmer', 'date_needed', 'payment_mode', 'payment_method')
