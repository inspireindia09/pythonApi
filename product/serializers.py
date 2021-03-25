from rest_framework import serializers
from .models import ProductDetail

#Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductDetail
        fields='__all__'
  