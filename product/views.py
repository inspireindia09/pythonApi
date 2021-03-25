from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import ProductDetail
from .serializers import ProductSerializer
from rest_framework.response import Response
import json
from rest_framework import status ,mixins
#Product view
class ProductView(generics.GenericAPIView, mixins.CreateModelMixin,mixins.ListModelMixin):        
    queryset=ProductDetail.objects.all()
    serializer_class=ProductSerializer
    #permission_classes = (IsSuperUser,)
   
    def get(self,request,id=None):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
    def delete(self,request):
        id=self.request.query_params.get('id')
        ProductDetail.objects.get(id=id).delete()
        return Response({"message":"Success"})

class ProductCreateApi(generics.CreateAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductSerializer

class ProductApi(generics.ListAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteApi(APIView):
    def delete(self,request):
        id=self.request.query_params.get('id')
        ProductDetail.objects.get(id=id).delete()
        return Response({"message":"Success"})
