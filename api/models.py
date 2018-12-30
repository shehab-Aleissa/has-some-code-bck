from django.db import models
from django.contrib.auth.models import User

import datetime


# class Category(models.Model):
#     name = models.CharField(max_length=120)
    
#     def __str__(self):
#         return self.name


class Brand(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class ModelOfBrand(models.Model):
    category = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class SellingPost(models.Model):
    name = models.CharField(max_length=120)

class Post(models.Model):
    category = models.ForeignKey(SellingPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    img0 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img1 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img2 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img3 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img4 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img5 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img6 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    viewers = models.PositiveIntegerField(default=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelOfBrand, on_delete=models.CASCADE)
    contact_number = models.BigIntegerField(blank=True, null=True)
    whatsapp_number = models.BigIntegerField(blank=True, null=True)
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
        ('Manual', 'Manual'),
        ('Tiptronic', 'Tiptronic')
    ]
    transmission = models.CharField(max_length=120, choices=TRANSMISSION_CHOICES, blank=True, null=True)

    ##############################PRICE##################################
    price = models.IntegerField(blank=True, null=True)
    price_is_hidden = models.BooleanField(default=False)

    ##############################KILOMETER##################################
    Kilometer = models.IntegerField(blank=True, null=True)
  
    CONVERTABLE_CHOICES = [
        ('Regular', 'Regular'),
        ('Convertable', 'Convertable')
    ]
    roof_type = models.CharField(max_length=120, choices=CONVERTABLE_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return str(self.id)


class SpecialPost(models.Model):
    category = models.ForeignKey(SellingPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    img0 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img1 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img2 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img3 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img4 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img5 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    img6 = models.ImageField(upload_to = 'posts_img', blank=True, null=True)
    viewers = models.PositiveIntegerField(default=1)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(ModelOfBrand, on_delete=models.CASCADE)
    contact_number = models.BigIntegerField(blank=True, null=True)
    whatsapp_number = models.BigIntegerField(blank=True, null=True)
    email_address = models.CharField(max_length=250, blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    is_freezed = models.BooleanField(default=False)
    price = models.IntegerField(blank=True, null=True)
    price_is_hidden = models.BooleanField(default=False)

    CONVERTABLE_CHOICES = [
        ('Regular', 'Regular'),
        ('Convertable', 'Convertable')
    ]
    roof_type = models.CharField(max_length=120, choices=CONVERTABLE_CHOICES, blank=True, null=True)

    ##############################PRICE##################################
    

    ##############################KILOMETER##################################
    Kilometer = models.IntegerField(blank=True, null=True)
        
    ##############################TRANSMISSION##################################
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
        ('Tiptronic', 'Tiptronic')
    ]
    transmission = models.CharField(max_length=120, choices=TRANSMISSION_CHOICES, blank=True, null=True)

    ##############################YEARS##################################
    YEAR_CHOICES = []
    for r in range(1940, (datetime.datetime.now().year+2)):
        YEAR_CHOICES.append((r,r))
    year_of_made = models.IntegerField(choices=YEAR_CHOICES)

    wish_to_answer = models.BooleanField(default=False)
    FIRST_OWNER_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Second owner', 'Second wner'),
        ("Don't know", "Don't know"),
    ]
    first_owner = models.CharField(max_length=120, choices=FIRST_OWNER_CHOICES, blank=True, null=True)

    KUWAIT_AGENT_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    kuwait_agent = models.CharField(max_length=120, choices=KUWAIT_AGENT_CHOICES, blank=True, null=True)

    UNDER_WARRANTY_CHOICES = [
        ('Yes','Yes'),
        ('No', 'No')
    ]
    under_warranty = models.CharField(max_length=120, choices=UNDER_WARRANTY_CHOICES, blank=True, null=True)

    ACCIDENTS_CHOICES = [
        ('yes', 'yes'),
        ('No', 'No'),
        ("Don't know", "Don't know")
    ]
    accidents = models.CharField(max_length=120, choices=ACCIDENTS_CHOICES, blank=True, null=True)

    CAR_REPAINTED_CHOICES = [
        ('yes', 'yes'),
        ('No', 'No'),
        ('General paint', 'General paint'),
        ('Some parts', 'Some parts')
    ]
    repainted = models.CharField(max_length=120, choices=CAR_REPAINTED_CHOICES, blank=True, null=True)

    CAR_CONDITION_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Very good', 'Very good'),
        ('Good', 'Good'),
        ('acceptable', 'acceptable'),
        ('bad', 'bad')
    ]
    condition = models.CharField(max_length=120, choices=CAR_CONDITION_CHOICES, blank=True, null=True)

    EXAMINATION_CLAUSE_CHOICES = [
        ('yes', 'yes'),
        ('No', 'No'),
    ]
    examination_clause = models.CharField(max_length=120, choices=EXAMINATION_CLAUSE_CHOICES, blank=True, null=True)

    acceptable_min_price = models.CharField(max_length=250, blank=True, null=True)
    visible_defects = models.CharField(max_length=250, blank=True, null=True)
    car_specs = models.TextField(blank=True, null=True)
    other_comments = models.TextField(blank=True, null=True)

    TEAM_CONTACTING_CHOICES = [
        ('Phone', 'Phone'),
        ('Whatsapp', 'Whatsapp'),
        ('Email', 'Email')
    ]
    examination_clause = models.CharField(max_length=120, choices=EXAMINATION_CLAUSE_CHOICES, blank=True, null=True)

