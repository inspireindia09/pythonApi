# Generated by Django 2.2.6 on 2019-10-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20191021_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='centers',
            name='center_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='centers',
            name='center_long',
            field=models.FloatField(null=True),
        ),
    ]