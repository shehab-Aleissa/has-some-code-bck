from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView ,
    ListAPIView,
    RetrieveUpdateAPIView ,
    DestroyAPIView)

from .models import Category, SellingBrandsCategory, Post

from .serializers import CategorySerializer, SellingCategorySerializer, RegisterSerializer, PostSerializer
# Create your views here.


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

class CategoriesList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Selling(ListAPIView):
    queryset = SellingBrandsCategory.objects.all()
    serializer_class = SellingCategorySerializer

class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer