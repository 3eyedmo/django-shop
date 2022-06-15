from django.http import JsonResponse
from django.views import generic
from django.db.models import F
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics, serializers
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.exceptions import NotFound


from products.models import Product
from cart.models import Order, OrderStatus, CartItem
from cart.data_validation import CartItemDataClass


def add_cart(request):
    data = request.POST.dict()
    try:
        data.pop('csrfmiddlewaretoken')
        item = CartItemDataClass(**data)
        if item.is_valid():
            item.save(user=request.user)
            return JsonResponse(data={"data":{
                "product":item.product_id,
                "quentity":item.quentity
            }})
        return JsonResponse(data={"error_message": item.error_message})
    except:
        return JsonResponse(data={"error_message": "", "status":400}, status=400)

    
class ListCartItems(LoginRequiredMixin, generic.ListView):
    template_name = "cart/index.html"

    def get_queryset(self):
        user = self.request.user
        qs = CartItem.objects.for_user(user=user).select_related('product')
        return qs



class OrderDefalutValue:
    requires_context = True

    def __call__(self, serializer_field):
        value = serializer_field.context.get("order")
        print("This is order from validator : ", value)
        return serializer_field.context.get("order")



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


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.order.user


class CreateCartItem(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = CartItemSerializer

    def get_serializer_context(self):
        data = super().get_serializer_context()
        data.update({
            "user": self.request.user,
            "order": self.get_order()
        })
        return data

    def get_order(self):
        order, _ = Order.objects.get_or_create({
            "user":self.request.user,
            "status":OrderStatus.Pending
        })
        return order

from rest_framework import mixins
from rest_framework.response import Response

class RetrieveUpdateDestroyCartItem(
    generics.GenericAPIView
):
    queryset = CartItem.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = CartItemSerializer
    http_method_names = ['patch', 'delete']
    lookup_field = "pk"

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, partial = True)
        serializer.is_valid(raise_exception=True)
        instance = self.get_object()
        cart = serializer.update(instance, serializer.validated_data)
        return Response(
            data={
                "quentity": cart.quentity
            },
            status=200
        )

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)









