from rest_framework import serializers
from .models import Centers,Category,Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'