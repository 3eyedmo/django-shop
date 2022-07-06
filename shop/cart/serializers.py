from django.db.models import F

from rest_framework import serializers

from cart.models import CartItem
from cart.validators import ProductValidator, QuentityValidator


class OrderDefalutValue:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context.get("order")


class CartItemAddOrCreateSerializer(serializers.ModelSerializer):
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

    def update(self, validated_data):
        instance = self.instance
        quentity = validated_data.get("quentity", instance.quentity)
        instance.quentity = quentity
        instance.save()
        return instance
    
    def validate(self, attrs):
        data = super().validate(attrs)
        quentity = data.get("quentity")
        product = data.get("product")
        request = self.context.get("request")

        if request.method.lower() != "post":
            validator = QuentityValidator(
                self.instance.product.valid_order_number
            )
        else:
            validator = QuentityValidator(
                product.valid_order_number
            )

        validator(quentity)
        return data

    def save(self, *args, **kwargs):
        user = self.context.get("request").user
        product = self.validated_data.get("product")
        quentity = self.validated_data.get("quentity")
        order = self.validated_data.get("order")
        if CartItem.objects.for_user(user).filter(product=product).exists():
            cart = CartItem.objects.for_user(user).get(product=product)
            sum_of_quentities = cart.quentity + quentity
            print("sum of products :  ", sum_of_quentities)
            if sum_of_quentities > product.valid_order_number:
                raise serializers.ValidationError("total number is bigger than")
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



    