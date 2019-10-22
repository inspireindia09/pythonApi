from rest_framework import serializers
from .models import Centers,Category,Product,Video
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class CategoryRelatedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Centers
        fields='__all__'