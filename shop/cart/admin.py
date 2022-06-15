from django.contrib import admin


from cart.models import CartItem, Order

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

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "status",
        "created",
        "updated"
    ]