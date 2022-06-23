from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models import Q, F

from orders.models_status import OrderStatus




class CartManager(models.Manager):
    def for_user(self, user):
        pending_query = Q(order__status=OrderStatus.Pending)
        user_query = Q(order__user = user)
        qs = super().get_queryset().filter(
            pending_query & user_query
        )
        return qs
        


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
        'orders.Order',
        related_name="items",
        on_delete=models.SET_NULL,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = CartManager()

    def total_info(self):
        info = {
            "total_price": F("product__price") * F("quentity")
        }
        

    def __str__(self):
        return f"{self.quentity} , order:  "

    class Meta:
        verbose_name = _('cart item')
        verbose_name_plural = _('cart items')
    