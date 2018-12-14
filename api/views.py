from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView ,
    ListAPIView,
    RetrieveUpdateAPIView ,
    DestroyAPIView)

from .models import SellingBrandsCategory, Post, ClassesOfTheBrand

from .serializers import SellingBrandsSerializer, RegisterSerializer, PostSerializer, BrandClassSerializer
# Create your views here.


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

    # GETS THE SELLING BRANDS
class SellingBrands(ListAPIView):
    queryset = SellingBrandsCategory.objects.all()
    serializer_class = SellingBrandsSerializer

    # GETS ALL THE POSTS IN THE DATABASE
class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # GETS THE LATEST (5) POSTS IN THE DATABASE
class LatestPosts(ListAPIView):
    queryset = Post.objects.all().order_by('-posted_on')[:5]
    serializer_class = PostSerializer

    # GETS THE MOST (5) POSTS IN THE DATABASE
class MostViewed(ListAPIView):
    queryset = Post.objects.all().order_by('-viewers')[:5]
    serializer_class = PostSerializer

    # DO THE FUNCTIONALITY OF THE VIEWERS COUNT
class ViewsCount(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, post_id, format=None):
        post = Post.objects.get(id=post_id)
        post.viewers += 1
        post.save()
        return Response(post.viewers)

    # GETS ONLY THE POSTS RELATED TO THE BRAND THAT HAVE BEEN CHOOSEN IN THE FRONTEND
class BrandsPosts(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        brand_id = self.kwargs['brand_id']
        brand = SellingBrandsCategory.objects.get(id=brand_id)
        return brand.post_set.all()
   

class BrandClass(ListAPIView):
    serializer_class = BrandClassSerializer

    def get_queryset(self, *args, **kwargs):
        brand_id = self.kwargs['brand_id']
        brand = SellingBrands.objects.get(id=brand_id)
        return brand.classesofthebrand_set.all()


