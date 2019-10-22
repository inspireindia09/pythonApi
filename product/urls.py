from django.contrib import admin
from django.urls import path,include
from .views import ProductDetails,CategoryRelatedVideo,Search
urlpatterns = [
    path('productlist/', ProductDetails.as_view()),
    path('videos/', CategoryRelatedVideo.as_view()),
    path('search/',Search.as_view())
]