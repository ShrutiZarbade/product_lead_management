from rest_framework import serializers

from .models import LeadManagement, ProductManagement


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManagement
        fields = '__all__'
    
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadManagement
        fields = ['id', 'name', 'email', 'phone_number', 'created_at']

