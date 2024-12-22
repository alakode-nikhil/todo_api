from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserRegistrationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(required = True, validators = [UniqueValidator(queryset=User.objects.all(), message="Username already exists.")])
    email = serializers.EmailField(required = True, validators = [UniqueValidator(queryset=User.objects.all(), message="Email already exists.")])
    password = serializers.CharField(write_only = True, style ={'input_type':'password'})

    class Meta:
        model = User
        fields = ['username','email','password']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style = {'input_type':'password'}, write_only = True)