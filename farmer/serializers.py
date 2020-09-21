from rest_framework import serializers
from .models import Group, FarmerProfile
from django.contrib.auth.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'description', 'logo', 'address', 'contact_person', 'contact_person_email', 
        'contact_person_phone')


class FarmerProfileSerializer(serializers.ModelSerializer):
    sector = serializers.PrimaryKeyRelatedField(many=False, queryset=FarmerProfile.objects.all())
    class Meta:
        model = FarmerProfile
        fields = ('user', 'date_of_birth', 'nin', 'sector', 'region', 'district', 'county', 
        'sub_county', 'region', 'parish', 'village', 'level_of_education', 'marital_status', 
        'size_of_land', 'phone_1', 'phone_2', 'group', 'type_of_land', 'production_scale', 'number_of_dependants',
        'credit_access', 'experience', 'status', 'general_remarks', 'approver', 'approved_date')