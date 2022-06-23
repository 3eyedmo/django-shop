from django.db import models
from django.db.models import Sum, F
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from orders.models_status import OrderStatus


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

    def total_price(self):
        price = self.items.aggregate(total_cost=Sum("product__price") * F("quentity"))
        return price.get("total_cost")

    @property
    def item_detail(self):
        items = self.items.annotate(total_item_cost = F("quentity") * F("product__price"))
        return items


    class Meta:
        verbose_name = _('user order')
        verbose_name_plural = _('user orders')


class PendingOrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = OrderStatus.Pending)


class PendingOrder(Order):
    objects = PendingOrderManager()

    class Meta:
        proxy = True


class DoneOrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = OrderStatus.Done)


class DoneOrder(Order):
    objects = DoneOrderManager()

    class Meta:
        proxy = True