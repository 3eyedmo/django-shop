from rest_framework import serializers
from rest_framework.exceptions import NotFound

from products.models import Product

class QuentityValidator:
    max_quentity = 10

    def __call__(self, quentity):
        if quentity > self.max_quentity:
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