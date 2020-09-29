from rest_framework import serializers
from .models import Group, FarmerProfile
from django.contrib.auth.models import User
from farm .models import Sector
from common .serializers import UserSerializer


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('name', 'description', 'logo', 'address', 'contact_person', 'contact_person_email', 
        'contact_person_phone')


class FarmerProfileSerializer(serializers.ModelSerializer):
    #sector = serializers.PrimaryKeyRelatedField(many=True, queryset=Sector.objects.all())
    sector = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    user = serializers.SlugRelatedField(many=False,read_only=True, slug_field='username')
    region = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    district = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    county = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    sub_county = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    parish = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    village = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    group = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    credit_access = serializers.SerializerMethodField(method_name='conversion_bool',source='Credit access')

    class Meta:
        model = FarmerProfile
        fields = ('id','user', 'date_of_birth', 'nin', 'sector', 'region', 'district', 'county', 
        'sub_county', 'region', 'parish', 'village', 'level_of_education', 'marital_status', 
        'size_of_land', 'phone_1', 'phone_2', 'group', 'type_of_land', 'production_scale', 'number_of_dependants',
        'credit_access', 'experience', 'status', 'general_remarks', 'approver', 'approved_date')
    '''
    returns yes or no for boolean fields
    '''
    def conversion_bool(self, instance):
        if instance.credit_access == True:
            return "Yes"
        else:
            return "No"
       
    
class FarmerApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProfile
        fields =('status','approver','approved_date')