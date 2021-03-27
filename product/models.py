from django.db import models
from cloudinary.models import CloudinaryField
from datetime import date
#Product detail model
class ProductDetail(models.Model):
    product_name=models.CharField(max_length=100)
    product_image_name=models.CharField(max_length=100)
    product_image=CloudinaryField('image')
    last_update=models.DateField(default=date.today)
    def __str__(self):
        return self.product_name

