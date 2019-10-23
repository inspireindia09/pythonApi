from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from .models import Category,Centers,Product,Video
from .serializers import ProductSerializer,CategoryRelatedVideoSerializer, CenterSerializer
from rest_framework.response import Response
import json
#import geocoder from setting in setting file we set the api key
from engineerbabu.settings import geocoder

#Product detail but in future we can get product not only heath related but also with other category also
class ProductDetails(generics.ListAPIView):
    serializer_class=ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(product_category='Health') 

#user get video for get knowledge i create this based on category suppose now its health in future we can get video with other cateogry also
class CategoryRelatedVideo(generics.ListAPIView):
    serializer_class=CategoryRelatedVideoSerializer

    def get_queryset(self):
        return Video.objects.filter(video_category='Health')

#Search based on location and distance
class Search(APIView):
  
    def get(self,request):
  
        #here calling get_address_detail method and inside paranthesis we are getting locaiton of user coming from frontend and we pass as argument .
        
        location=self.get_address_details(self.request.query_params.get('location'))
  
        #if we enter wrong locaiton like 'aaaaaaaa' then if condion will execute if location found then else block execute
        if location is None:
            return Response({"Massage":"The location you passed that is not available please check location then try","status":status.HTTP_404_NOT_FOUND}) 
        else:
            #Check category like health or fitness if found then else block execute otherwise if block
            category_found_or_not=self.get_category(self.request.query_params.get('category'))
            
            #check condition category found or  not
            if category_found_or_not=='Not Found':
                return Response({"massage":"The Category you entere that is not available","status":status.HTTP_404_NOT_FOUND})
            else:
                #Get centers based on category
                centers=Centers.objects.filter(center_category=category)
            
                #creating a dictionary here 
                data = []
                for center in centers:
                    database_location=center.center_location
                    database_location_data=self.get_address_details(database_location)

                    #User location details , i got here location latitude and longitude
                    lat1 = location.latitude
                    lon1 = location.longitude

                    # Centers locaiton latitude and longitude
                    lat2 = database_location_data.latitude
                    lon2 = database_location_data.longitude

                    # calculating the distance
                    dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
                    
                    #In if condition i set max 50 km distance if future we can update distance whatever we want 
                    if(dist<=50.00):
                        data.append({"center_name": center.center_name, "center_location":center.center_location , "center_category": center.center_category})
                       
                    else:
                        return Response({"massage":"No Center available in your area.","status":status.HTTP_200_OK})  

                #dump dictionary  into json this json should be return to the user.       
                json_data=json.dumps(data)
                return Response(json_data)

    #In this method ,method return the location detail like latitude , longitude    
    def get_address_details(self,address):
        search = geocoder.get(address)
        return search

    #this method is called to return category available in database or not    
    def get_category(self,category):
        try:
            found = Centers.objects.get(center_category=category)
            return found
        except Centers.DoesNotExist:
            return "Not Found"