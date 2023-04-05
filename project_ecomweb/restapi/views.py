from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import CategorySerializer, ProductSerializer
from app_ecom.models import Category, Product

# Create your views here.
class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)

class ProductApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        product_serialize = ProductSerializer(products, many=True)
        return Response(product_serialize.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        product_serialize = ProductSerializer(data=data)
        if product_serialize.is_valid():
            product_serialize.save()
            return Response({"msg": "Product added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(product_serialize.errors, status=status.HTTP_400_BAD_REQUEST)