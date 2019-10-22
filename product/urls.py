from django.contrib import admin
from django.urls import path,include
from .views import ProductDetails
urlpatterns = [
    path('productlist/', ProductDetails.as_view()),
    # path('products/', include('product.urls'))
]