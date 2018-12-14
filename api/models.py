from django.db import models
from django.contrib.auth.models import User

import datetime


# class Category(models.Model):
#     name = models.CharField(max_length=120)
    
#     def __str__(self):
#         return self.name


class SellingBrandsCategory(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class ClassesOfTheBrand(models.Model):
    category = models.ForeignKey(SellingBrandsCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    viewers = models.PositiveIntegerField(default=1)
    brand = models.ForeignKey(SellingBrandsCategory, on_delete=models.CASCADE)
    brand_class = models.ForeignKey(ClassesOfTheBrand, on_delete=models.CASCADE)
    extra_phone_number = models.BigIntegerField(blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    is_freezed = models.BooleanField(default=False)

    ##############################YEARS##################################
    YEAR_CHOICES = []
    for r in range(1940, (datetime.datetime.now().year+2)):
        YEAR_CHOICES.append((r,r))
    year_of_made = models.IntegerField(choices=YEAR_CHOICES)
    ##############################TRANSMISSION##################################
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual')
    ]
    transmission = models.CharField(max_length=120, choices=TRANSMISSION_CHOICES, blank=True, null=True)
    ##############################EXTERIOR COLOR##################################
    COLOR_CHOICES = [
        ('White', 'White'),
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Pink', 'Pink'),
        ('Purple', 'Purple'),
        ('Tan', 'Tan'),
        ('Brown', 'Brown'),
        ('Grey', 'Grey'),
    ]
    exterior_color = models.CharField(max_length=120, choices=COLOR_CHOICES, blank=True, null=True)
    ##############################INTERIOR COLOR##################################
    COLOR_CHOICES = [
        ('White', 'White'),
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Pink', 'Pink'),
        ('Purple', 'Purple'),
        ('Tan', 'Tan'),
        ('Brown', 'Brown'),
        ('Grey', 'Grey'),
    ]
    interior_color = models.CharField(max_length=120, choices=COLOR_CHOICES, blank=True, null=True)
    ##############################PRICE##################################
    price = models.IntegerField(blank=True, null=True)
    price_is_hidden = models.BooleanField(default=False)

    ##############################KILOMETER##################################
    Kilometer = models.IntegerField(blank=True, null=True)

    ##############################BODY TYPE##################################
    BODY_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Pickup Truck', 'Pickup Truck'),
        ('Sport', 'Sport'),
        ('MicroCar', 'MicroCar'),
        ('Van', 'Van'),
        
    ]
    body_type = models.CharField(max_length=120, choices=BODY_TYPE_CHOICES, blank=True, null=True)
    
    ##############################SUN ROOF##################################
    SUNROOF_CHOICES = [
        ('No', 'No'),
        ('Normal', 'Normal'),
        ('Panorama', 'Panorama'),
    ]
    sunroof = models.CharField(max_length=120, choices=SUNROOF_CHOICES, blank=True, null=True)

    CONVERTABLE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]
    convertable = models.CharField(max_length=120, choices=CONVERTABLE_CHOICES)
    
    def __str__(self):
        return str(self.id)


# class Images(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     image = models.ImageField(blank=True, null=True)





        


