# Create your models here.

from django.db import models
from decimal import Decimal

class ProductManagement(models.Model):
    name = models.CharField(max_length=255)  # String
    description = models.TextField()  # Text
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))  # Decimal
    created_at = models.DateTimeField(auto_now_add=True)  # DateTime (auto-generated)
    updated_at = models.DateTimeField(auto_now=True)  # DateTime (auto-updated)

class LeadManagement(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=13)
    interested_products = models.ManyToManyField(ProductManagement, related_name='leads')
    created_at = models.DateTimeField(auto_now_add=True)