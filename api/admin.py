from django.contrib import admin
from .models import Category, SellingBrandsCategory, Post
# Register your models here.
admin.site.register(Category)
admin.site.register(SellingBrandsCategory)
admin.site.register(Post)