from django.db import models

#Category is like health product or other product model
class Category(models.Model):
    category_name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.category_name

#Product detail model
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.IntegerField(default=0)
    product_detail=models.TextField()
    product_category=models.ForeignKey(Category,on_delete=models.CASCADE,to_field="category_name")
    #For future we can upload image and display acutally i did not upload image because heroku delete image after some time.
    #product_picture=models.FileField(upload_to='Media/')
    def __str__(self):
        return self.product_name

#Centers
class Centers(models.Model):
    center_name=models.CharField(max_length=100)
    center_location=models.CharField(max_length=100)
    center_category=models.CharField(max_length=100)
    
    def __str__(self):
        return self.center_name

#Vidoes for user so they can be educated
class Video(models.Model):
    video_title=models.CharField(max_length=100)
    video_category=models.ForeignKey(Category,on_delete=models.CASCADE, to_field='category_name')
    video_article=models.TextField()
    video_link=models.URLField() 
    
    def __str__(self):
        return self.video_title
