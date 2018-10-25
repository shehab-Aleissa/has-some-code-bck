from django.db import models
from django.contrib.auth.models import User

import datetime


class Category(models.Model):
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name


class SellingBrandsCategory(models.Model):
    category = models.ForeignKey(Category, related_name='brands', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    brand = models.ForeignKey(SellingBrandsCategory, on_delete=models.CASCADE)
    ##############################YEARS##################################
    YEAR_CHOICES = []
    for r in range(1940, (datetime.datetime.now().year+2)):
        YEAR_CHOICES.append((r,r))
    year_of_made = models.IntegerField(choices=YEAR_CHOICES, blank=True, null=True)
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

    ##############################KILOMETER##################################
    Kilometer = models.IntegerField(blank=True, null=True)

    ##############################BODY TYPE##################################
    BODY_TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
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

    ##############################ADDED##################################
    added = models.DateTimeField(auto_now_add=True, blank=True)

    
    def __str__(self):
        return str(self.id)





        


