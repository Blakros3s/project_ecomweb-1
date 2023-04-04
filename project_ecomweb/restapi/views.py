from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import CategorySerializer
from app_ecom.models import Category

# Create your views here.
class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializer(categories, many=True)
        return Response(category_serializer.data, status=status.HTTP_200_OK)