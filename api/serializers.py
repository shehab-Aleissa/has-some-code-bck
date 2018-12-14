from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from .models import SellingBrandsCategory, Post, ClassesOfTheBrand



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
    # category = serializers.SerializerMethodField()
    # posts = serializers.SerializerMethodField()

    # def get_category
    class Meta:
        model = SellingBrandsCategory
        fields = '__all__'

class BrandClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassesOfTheBrand
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    brand = SellingBrandsSerializer()
    brand_class = BrandClassSerializer()
    class Meta:
        model = Post
        fields = '__all__'


    # def get_posts(self, obj):
    #     posts = obj.post_set.all()
    #     return PostSerializer(posts, many=True, context=self.context).data  

# class BrandsPostsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SellingBrandsCategory
#         fields = '__all__'
    
# class CategorySerializer(serializers.ModelSerializer):
#     brands = serializers.SerializerMethodField()


#     class Meta:
#         model = Category
#         fields = '__all__'
    
    
#     def get_brands(self, obj):
#         brands = obj.brands.all()
#         return SellingCategorySerializer(brands, many=True, context=self.context).data



