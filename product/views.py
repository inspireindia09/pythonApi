from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Category,Centers,Product,Video
from .serializers import ProductSerializer,CategoryRelatedVideoSerializer
from rest_framework.response import Response
# Get Product details

class ProductDetails(generics.ListAPIView):
    serializer_class=ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(product_category='Health') 

class CategoryRelatedVideo(generics.ListAPIView):
    serializer_class=CategoryRelatedVideoSerializer

    def get_queryset(self):
        return Video.objects.filter(video_category='Health')
