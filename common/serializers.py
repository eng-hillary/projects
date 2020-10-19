from rest_framework import serializers
from django.contrib.auth.models import User,Group
from .models import Region, District, County, SubCounty, Parish, Village


class GroupSerializer(serializers.Serializer):
    permissions = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    name = serializers.CharField()
    
    class Meta:
        model = Group
        fields = ['name','permissions']


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    user_permissions = serializers.SlugRelatedField(many=True,read_only=True, slug_field='name')
    groups = GroupSerializer(many=True)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    full_name = serializers.SerializerMethodField(method_name='get_user_full_name',source='username')
    phone_number = serializers.CharField(source='profile.phone_number')
    gender = serializers.CharField(source='profile.get_gender_display')
    home_address = serializers.CharField(source='profile.home_address')
    profile_pic = serializers.FileField(source='profile.profile_pic')
    region = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    district = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    county = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    sub_county = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    parish = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')
    village = serializers.SlugRelatedField(many=False,read_only=True, slug_field='name')

    def get_user_full_name(self, obj):
        return '{} {}'.format(obj.first_name, obj.last_name)

    class Meta:
        model = User
        exclude =['password1']


class DistrictSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = District
        fields ='__all__'


class CountySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = County
        fields ='__all__'

class SubCountySerializer(serializers.ModelSerializer):
  
    class Meta:
        model = SubCounty
        fields ='__all__'

class ParishSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Parish
        fields ='__all__'

class VillageSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Village
        fields ='__all__'