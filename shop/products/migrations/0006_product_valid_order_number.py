# Generated by Django 4.0.5 on 2022-06-30 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_image_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='valid_order_number',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]