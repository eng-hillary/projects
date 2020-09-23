from rest_framework import serializers
from django.contrib.auth.models import User,Group


class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)