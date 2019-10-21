from django.db import models

#Category is like health product or other product model
class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)

#Product detail model
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField(default=0)
    product_detail=models.TextField()
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE,to_field="category_name")

     
