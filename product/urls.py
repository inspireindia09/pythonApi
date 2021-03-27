from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    path('product/', ProductView.as_view()),  #get product list based on category
    path('api',ProductApi.as_view()),
    path('api/create',ProductCreateApi.as_view()),
    path('api/<int:pk>',ProductUpdateApi.as_view()),
    path('api/delete',ProductDeleteApi.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here

]