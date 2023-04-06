from rest_framework import serializers
from app_ecom.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'category_name',]
        model = Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'desc', 'category', 'price', 'quantity', 'cod', 'discount', 'user']
        model = Product