from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models import Q


class OrderStatus(models.TextChoices):
    Pending = "P"
    Done = "D"
    Failed = "F"


class CartManager(models.Manager):
    def for_user(self, user):
        pending_query = Q(order__status=OrderStatus.Pending)
        user_query = Q(order__user = user)
        qs = super().get_queryset().filter(
            pending_query & user_query
        )
        return qs
        


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("order user"),
        related_name="orders",
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        verbose_name=_("order status"),
        max_length=250,
        choices=OrderStatus.choices,
        default=OrderStatus.Pending
    )
    created = models.DateTimeField(
        verbose_name=_("creation time"),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_("modification time"),
        auto_now=True
    )
    

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = _('user order')
        verbose_name_plural = _('user orders')



class CartItem(models.Model):
    product = models.ForeignKey(
        'products.Product',
        related_name="cart",
        on_delete=models.SET_NULL,
        null=True
    )
    quentity = models.SmallIntegerField(
        verbose_name=_('quentity'),
        default=1
    )
    order = models.ForeignKey(
        'cart.Order',
        related_name="items",
        on_delete=models.SET_NULL,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CartManager()

    def __str__(self):
        return f"{self.quentity} , order:  "

    class Meta:
        verbose_name = _('cart item')
        verbose_name_plural = _('cart items')
    