from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# altina
# class User(AbstractUser):
#     is_client = models.BooleanField(default=False)
#     is_company = models.BooleanField(default=False)
#     phone_number = models.CharField(max_length=30)
#     location = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)
#
#
# class Company(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     name = models.CharField(max_length=80)
#     logo = models.ImageField(blank=True)
#
#
# class Client(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     first_name = models.CharField(max_length=80)
#     last_name = models.CharField(max_length=80)
#
#
# # /altina
#
# class Category(models.Model):
#     category_name = models.CharField(max_length=255)
#
#
# class SubCategory(models.Model):
#     subcategory_name = models.CharField(max_length=255)
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)
#
#
# # Esma
# class Product(models.Model):
#     name = models.CharField(max_length=80)
#     product_type = models.CharField(max_length=128)
#     image = models.ImageField(blank=True)
#     description = models.TextField()
#     exp_date = models.DateField()
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=20, decimal_places=2)
#     created = models.DateTimeField(default=datetime.now, blank=True)
#     category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
#     company = models.ForeignKey(Company, on_delete=models.PROTECT)
#
#
# # /Esma

class PriceHistory(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=20)
    created = models.DateTimeField()
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)


