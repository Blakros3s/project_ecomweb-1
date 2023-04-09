from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import CategorySerializer, ProductSerializer
from app_ecom.models import Category, Product

# Create your views here.
class ApiResponse():
    def successResponse(self, message, code, data=dict()):
        context = {
                "message": message,
                "status_code": code,
                "data": data,
                "error": []
            }
        return context

class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)

class ProductApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        try:
            product_serialize = ProductSerializer(products, many=True)
            response = ApiResponse()
            return Response(response.successResponse(message="Product List", code=200, data=product_serialize.data), status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            context = {
                "message": "Product Not found",
                "status_code": 404,
                "data": [],
                "error": {"error_message": "Data not found"}
            }
            return Response(context, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        product_serialize = ProductSerializer(data=data)
        if product_serialize.is_valid():
            product_serialize.save()
            return Response({"msg": "Product added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(product_serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductApiIdView(APIView):
    def get_object(self, id):
        """this function will return object of product"""
        try:
            product = Product.objects.get(id=id)
            return product
        except Product.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Something went wrong", "error": serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg": "Data deleted successfully"}, status=status.HTTP_200_OK)