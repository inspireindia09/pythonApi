from django.contrib import admin
from .models import ProductDetail
# Register your models here.
#we need to register model to show those model(table) in admin template
admin.site.register(ProductDetail)
