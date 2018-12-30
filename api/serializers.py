from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from .models import Brand, Post, ModelOfBrand, SpecialPost, SellingPost



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token', ]

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(new_user)
        token = jwt_encode_handler(payload)

        validated_data["token"] = token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

class SellingBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelOfBrand
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    brand = SellingBrandsSerializer()
    model = BrandClassSerializer()
    class Meta:
        model = Post
        fields = '__all__'

class SpecialPostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    brand = SellingBrandsSerializer()
    model = BrandClassSerializer()
    class Meta:
        model = SpecialPost
        fields = '__all__'


class AllPostsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SellingPost
        fields = '__all__'




