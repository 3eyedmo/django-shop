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
    category = models.ForeignKey(
        'Category',
        related_name='products',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("category")
    )
    name = models.CharField(_("name"), max_length=255)
    discription = models.TextField(_("discription"), max_length=2047)
    price = models.PositiveBigIntegerField(_("price"), null=True)
    quentity = models.IntegerField(_("quentity"), null=True)
    image = models.ImageField(_("image"), null=True, upload_to="images/")
    created = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self) -> str:
        return self.name + ', ' + self.category.name
