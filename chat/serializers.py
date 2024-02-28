from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *


class UserSerailizer(serializers.ModelSerializer):
    
    password=serializers.CharField(write_only=True)
    
    def create(self,validated_data):
        user=User.objects.create_user(email=validated_data['email'],password=validated_data['password'],first_name=validated_data.get('first_name',' '),last_name=validated_data.get('last_name',' '))
        return user
    
    
    class Meta:
        model=User
        fields=['email', 'password', 'first_name', 'last_name']
        extra_kwargs={'password':{'write_only':True}}
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    id=serializers.CharField(max_length=15,read_only=True)
    password=serializers.CharField(max_length=255,write_only=True)
    def validate(self, data):
        email=data.get("email",None)
        password=data.get("password",None)
        
        if email is None:
            raise serializers.ValidationError("An email address must be provided")
        if password is None:
            raise serializers.ValidationError("An password must be provided")
            
        user=authenticate(username=email,password=password)
        
        if user is None:
            raise serializers.ValidationError("Invalid Email or password")
        if not user.is_active:
            raise serializers.ValidationError("User is inactive")
        return {"email":user.email,"id":user.id}