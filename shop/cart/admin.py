from django.contrib import admin

from cart.models import CartItem



@admin.register(CartItem)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product",
        "quentity",
        "order",
        "created",
        "updated"
    ]
