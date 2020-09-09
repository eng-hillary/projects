from rest_framework import serializers
from .models import Group, FarmerProfile
from django.contrib.auth.models import User


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'description', 'logo', 'address', 'contact_person', 'contact_person_email', 
        'contact_person_phone')


class FarmerProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FarmerProfile
        fields = ('name', 'date_of_birth', 'nin', 'sector', 'region', 'district', 'county', 
        'sub-county', 'region', 'parish', 'village', 'level_of_eductaion', 'gender', 'marital_status', 
        'land_owned', 'phone_1', 'phone_2', 'group', 'type_of_land', 'production_scale', 'number_of_dependants',
        'credit_access', 'experience', 'status', 'general_remarks', 'approver', 'approved_date')