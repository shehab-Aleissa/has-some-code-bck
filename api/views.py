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

from .models import SellingBrandsCategory, Post

from .serializers import SellingBrandsSerializer, RegisterSerializer, PostSerializer
# Create your views here.


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer

class SellingBrands(ListAPIView):
    queryset = SellingBrandsCategory.objects.all()
    serializer_class = SellingBrandsSerializer

class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class BrandsPosts(ListView):
#     model = SellingBrandsCategory
#     serializer_class = BrandsPostsSerializer
    
#     def get_queryset(self):
#         return SellingBrandsCategory.objects.get(id=)

class ViewsCount(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, post_id, format=None):
        post = Post.objects.get(id=post_id)
        post.viewers += 1
        post.save()
        return Response(post.viewers)


class BrandsPosts(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        brand_id = self.kwargs['brand_id']
        brand = SellingBrandsCategory.objects.get(id=brand_id)
        return brand.post_set.all()
    # def get(self, request, brand_id):
    #     brand = SellingBrandsCategory.objects.get(id=brand_id)
    #     posts = brand.post_set.all()
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)


# class DetailedPosts(ListAPIView):

#     serializer_class = PostSerializer

#     def get_queryset(self):
        
#         post_id = self.kwargs['post_id']
#         return Post.objects.filter(id=post_id)

# class PostByBrand(ListAPIView):
#     def getBrandPost(self, request,post_id, *args, **kwargs, ):
#         brandPost = Post.objects.get(id=post_id)
#         return brandPost

#     def get_queryset(self):
#         queryset = Post.objects.get()
#         return queryset


