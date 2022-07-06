from rest_framework import serializers
from rest_framework.exceptions import NotFound

from products.models import Product

class QuentityValidator:

    def __init__(self, product_max_order):
        self.max_order = product_max_order

    def __call__(self, quentity):
        if quentity > self.max_order:
            raise serializers.ValidationError("quentity too much")
        return quentity



class ProductValidator:
    def __call__(self, id):
        existence = Product.objects.filter(id=id).exists()
        if not existence:
            raise NotFound("product doesn't exists!")
        try:
            product = Product.objects.get(id=id)
        except:
            raise NotFound("product doesn't exists!")

        return product