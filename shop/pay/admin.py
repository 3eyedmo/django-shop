from django.contrib import admin
from pay.models import Pay


@admin.register(Pay)
class PayAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "total_price",
        "order",
        "created",
        "updated"
    ]