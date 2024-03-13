from users.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.generics import ListCreateAPIView

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email','password']
        read_only_fields = ['id','username', 'email','password']

class UserSerializerChoose(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']
        read_only_fields = ['id','username', 'email']
        

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}, }
