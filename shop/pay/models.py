from django.db import models
from django.utils.translation import gettext_lazy as _

class Pay(models.Model):
    total_price = models.PositiveBigIntegerField(null=True)
    order = models.OneToOneField(
        'orders.Order',
        on_delete=models.PROTECT,
        related_name="pay",
        verbose_name=_("order")
    )
    created = models.DateTimeField(
        verbose_name=_("creation time"),
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name=_("modification time"),
        auto_now=True
    )

    def pay_related_form(self):
        order = self.order
        items = dict()
        for item in order.items:
            pass

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.total_cost = self.order.total_price()
            return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)

    
  
