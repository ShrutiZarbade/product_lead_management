# Create your models here.

from decimal import Decimal

from django.db import models


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
    created_at = models.DateTimeField(auto_now_add=True)

class ProductLead(models.Model):
    product = models.ForeignKey(ProductManagement, on_delete=models.CASCADE)
    lead = models.ForeignKey(LeadManagement, on_delete=models.CASCADE)
