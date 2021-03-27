# Generated by Django 2.2.6 on 2021-03-25 08:41

import cloudinary.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20191022_0411'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image_name', models.CharField(max_length=100)),
                ('product_image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('last_update', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.DeleteModel(
            name='Centers',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]