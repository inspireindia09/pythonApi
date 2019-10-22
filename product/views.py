from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import Category,Centers,Product,Video
from .serializers import ProductSerializer,CategoryRelatedVideoSerializer, CenterSerializer
from rest_framework.response import Response
import json
# Get Product details
from engineerbabu.settings import geocoder

class ProductDetails(generics.ListAPIView):
    serializer_class=ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(product_category='Health') 

class CategoryRelatedVideo(generics.ListAPIView):
    serializer_class=CategoryRelatedVideoSerializer

    def get_queryset(self):
        return Video.objects.filter(video_category='Health')

class Search(APIView):
    def get(self,request):
        address=self.request.query_params.get('location')
        location=self.get_address_details(address)
        print("lcoaion",location.latitude)
        if location is None:
            return Response({"Massage":"The location you passed that is not available please check location then try","status":status.HTTP_404_NOT_FOUND}) 
        else:
            centers=Centers.objects.all()
            print(centers)
            data = []
            for center in centers:
                print(center.center_location)
                database_location=center.center_location
                database_location_data=self.get_address_details(database_location)
                print('datbase',database_location_data.latitude)
                lat1 = location.latitude
                lon1 = location.longitude

                # Point two
                lat2 = database_location_data.latitude
                lon2 = database_location_data.longitude

                # What you were looking for
                dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
                print("distance=",dist)
                if(dist<=50.00):
                    data.append({"center_name": center.center_name, "center_location":center.center_location , "center_category": center.center_category})
                    print("if block")
                else:
                    print("elseblock")  
                   
            json_data=json.dumps(data)

            return Response(json_data)
        
    def get_address_details(self,address):
        search = geocoder.get(address)
        return search
