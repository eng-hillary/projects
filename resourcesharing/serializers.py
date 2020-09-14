from rest_framework import serializers
from .models import (Resource, ResourceSharing, ResourceBooking)


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['resource_name', 'owner', 'contacts', 'resource_category', 'latitude', 'longitude',
        'termsandconditions', 'resource_status', 'availability_date_and_time', 'price']

class ResourceSharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceSharing
        fields = ('resource', 'date_taken', 'expected_return_date', 'taken_by', 'phone_1', 'phone_2')


class ResourceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceBooking
        fields = ('resource', 'farmer', 'date_needed', 'payment_mode', 'payment_method')
