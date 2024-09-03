from rest_framework import serializers
from .models import ProductManagement,LeadManagement

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductManagement
        fields = '__all__'


class LeadSerializer(serializers.ModelSerializer):
    interested_products = ProductSerializer(many=True)

    class Meta:
        model = LeadManagement
        fields = ['id', 'name', 'email', 'phone_number', 'interested_products', 'created_at']

    def create(self, validated_data):
        products_data = validated_data.pop('interested_products')
        lead = LeadManagement.objects.create(**validated_data)
        for product_data in products_data:
            product, created = ProductManagement.objects.get_or_create(**product_data)
            lead.interested_products.add(product)
        return lead