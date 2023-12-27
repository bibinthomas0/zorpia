from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from rest_framework import serializers
from verification.models import CustomUser,Userdetails
from rest_framework_simplejwt.tokens import RefreshToken, Token,AccessToken
import random

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password')
        
class UserDetailsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userdetails
        fields = ['profile_pic']
        
        
        
class OtpRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
class OtpResponseSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
class EmailSerializer(serializers.Serializer):
    email = serializers.CharField()

class AdminRegisterSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','username','name','email','dob','password','userid','is_superuser']
        extra_kwargs = {
            'password':{ 'write_only':True}
        }
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        instance.is_superuser = True
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError({"password": "password is not valid"}) 
        

class UserRegisterSerializer(serializers.ModelSerializer):
    userid = serializers.CharField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','username','name','email','dob','password','userid']
        extra_kwargs = {
            'password':{ 'write_only':True}
        }
        
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
        else:
            raise serializers.ValidationError({"password": "password is not valid"}) 
        
        
        
class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','name','email','dob','password','userid',"created_at"]
        extra_kwargs = {
            'password':{ 'write_only':True}
        }