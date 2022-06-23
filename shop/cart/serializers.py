from django.db.models import F

from rest_framework import serializers

from cart.models import CartItem
from cart.validators import ProductValidator, QuentityValidator


class OrderDefalutValue:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context.get("order")


class CartItemSerializer(serializers.ModelSerializer):
    order = serializers.HiddenField(default = OrderDefalutValue())
    class Meta:
        model = CartItem
        fields = (
            'id',
            'order',
            'product',
            'quentity'
        )
        extra_kwargs = {
            "product": {
                "required":True
            } ,
            "id": {
                "read_only": True
            }
        }

    def update(self, instance, validated_data):
        quentity = validated_data.get("quentity", instance.quentity)
        instance.quentity = quentity
        instance.save()
        return instance

    def validate_product(self, product):
        validator = ProductValidator()
        return validator(product.id)

    def validate_quentity(self, quentity):
        validator = QuentityValidator()
        return validator(quentity)

    def save(self, *args, **kwargs):
        user = self.context.get("user")
        product = self.validated_data.get("product")
        quentity = self.validated_data.get("quentity")
        order = self.validated_data.get("order")
        
        if CartItem.objects.for_user(user).filter(product=product).exists():
            cart = CartItem.objects.for_user(user).get(product=product)
            sum_of_quentities = cart.quentity + quentity
            if sum_of_quentities > 10:
                raise serializers.ValidationError("total number bigger than 10")
            cart.quentity = F('quentity') + quentity
            cart.save()
            return cart

        cart = CartItem(
            order=order,
            product=product,
            quentity=quentity
        )
        cart.save()
        return cart