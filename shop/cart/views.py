from django.views import generic
from django.db.models import F
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response

from cart.models import CartItem
from cart.serializers import CartItemSerializer
from orders.models import Order, PendingOrder
from orders.models_status import OrderStatus
    

    
class ListCartItems(LoginRequiredMixin, generic.ListView):
    """
    This List View gives the list of cart items.
    """
    template_name = "cart/index.html"
    allow_empty: bool = True

    def get_queryset(self):
        user = self.request.user
        qs = CartItem.objects.for_user(user=user).select_related('product')
        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        if PendingOrder.objects.filter(user=user).exists():
            order = PendingOrder.objects.filter(user=user).order_by("-created").first()
            data["total_price"] = order.total_price()
        return data


class IsOwner(BasePermission):
    """
    This Permission checks if the current user is the order owner.
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.order.user


class CreateCartItem(generics.CreateAPIView):
    """
    This View creates Cart item.
    """
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
        order, _ = Order.objects.get_or_create(
            user = self.request.user,
            status = OrderStatus.Pending
        )
        return order



class RetrieveUpdateDestroyCartItem(
    generics.GenericAPIView
):
    """
    This View Retrieve, Update, Destroy a cart item.
    """
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
