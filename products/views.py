from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

# Create your views here.
from products.models import Product
from products.serializers import ProductSerializer


class ViewProducts(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AddProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class EditProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
