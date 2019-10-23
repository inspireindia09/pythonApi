from django.contrib import admin
from .models import Category,Product,Centers,Video
# Register your models here.
#we need to register model to show those model(table) in admin template
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Centers)
admin.site.register(Video)
