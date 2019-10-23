from django.contrib import admin
from django.urls import path,include
from .views import ProductDetails,CategoryRelatedVideo,Search
urlpatterns = [
    path('productlist/', ProductDetails.as_view()),  #get product list based on category
    path('videos/', CategoryRelatedVideo.as_view()), #get video related health
    path('search/',Search.as_view())                 #search based on location and distance
]