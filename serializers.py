from rest_framework import serializers
from landlord.models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['category','location','rooms','address','price','picture',]

