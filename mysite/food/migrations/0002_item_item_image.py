# Generated by Django 5.2 on 2025-05-05 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.shutterstock.com/image-vector/exciting-new-cafe-bar-restaurant-600nw-2145440019.jpg', max_length=500),
        ),
    ]
