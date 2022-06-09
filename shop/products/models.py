from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    discription = models.TextField(max_length=2047)
    price = models.BigIntegerField(null=True)
    quentity = models.IntegerField(null=True)
    image = models.ImageField(null=True, upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

