from rest_framework import serializers
from .models import ProductManagement,LeadManagement

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManagement
        fields = '__all__'
    
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadManagement
        fields = ['id', 'name', 'email', 'phone_number', 'created_at']

class ProductLeadCountSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField()
    lead_count = serializers.IntegerField()
