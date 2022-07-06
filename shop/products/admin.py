from django.contrib import admin

from products.models import Product, Category, ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'category',
        'price',
        'quentity',
        'created',
        'updated',
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'created',
    ]



@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "product"
    ]