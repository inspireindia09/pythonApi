# Generated by Django 2.2.6 on 2019-10-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(max_length=100)),
                ('center_location', models.CharField(max_length=100)),
                ('center_category', models.CharField(max_length=100)),
            ],
        ),
    ]
