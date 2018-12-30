from django.contrib import admin
from .models import Brand, Post, ModelOfBrand, SpecialPost, SellingPost
# Register your models here.
admin.site.register(Brand)
admin.site.register(SellingPost)
admin.site.register(Post)
admin.site.register(SpecialPost)
admin.site.register(ModelOfBrand)