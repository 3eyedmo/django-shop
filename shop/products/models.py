from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', related_name='products', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    discription = models.TextField(max_length=2047)
    price = models.PositiveBigIntegerField(null=True)
    quentity = models.IntegerField(null=True)
    image = models.ImageField(null=True, upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self) -> str:
        return self.name + ', ' + self.category.name

