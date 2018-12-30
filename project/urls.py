"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import SellingBrands, RegisterAPIView, SpecialPostList, PostList, AllSellingPostList, BrandsPosts, ViewsCount, LatestPosts, MostViewed, BrandClass
from django.conf.urls.static import static
from django.conf import settings
from api import views
from rest_framework_jwt.views import obtain_jwt_token
# from graphene_django.views import GraphQLView
# from schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', obtain_jwt_token, name='login'),

    # path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),

    # path('category/', CategoriesList.as_view(), name='category-list'),
    path('selling/brands/', SellingBrands.as_view(), name='sellingBrands-list'), 

    path('regular/posts/', PostList.as_view(), name='regular-posts'),
    path('special/posts', SpecialPostList.as_view(), name='special-posts'),
    path('all/posts', AllSellingPostList.as_view(), name='all-posts'),
    path('brand/posts/<int:brand_id>', BrandsPosts.as_view(), name='brand-posts'),
    path('brand/classes/<int:brand_id>', BrandClass.as_view(), name='brand-classes'),

    path('post/views/<int:post_id>', ViewsCount.as_view(), name='post-views'),
    path('latest/posts/', LatestPosts.as_view(), name='latest-posts'),
    path('most/viewed/posts/', MostViewed.as_view(), name='most-viewed-posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)