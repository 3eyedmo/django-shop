from django.shortcuts import redirect, render
from django.views import generic
from orders.models import Order
from orders.models_status import OrderStatus
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from pay.models import Pay

class VerifyPay(
    LoginRequiredMixin,
    generic.TemplateView
):
    template_name: str = "pay/verify/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        user = self.request.user
        order = get_object_or_404(Order, user=user, status = OrderStatus.Pending)
        data["total_price"] = order.total_price()
        return data


class CompletePay(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = self.request.user
        order = get_object_or_404(Order, user=user, status = OrderStatus.Pending)
        order.status = OrderStatus.Done
        order.save()
        pay = Pay(order=order, total_price=order.total_price())
        pay.save()
        messages.success(request=request, message="خرید مورد نظر با موفقیت انجام شد")
        return redirect("home:home")
        

class ListPays(LoginRequiredMixin, generic.ListView):
    template_name: str = "pay/pay_list/index.html"
    
    def get_queryset(self):
        pays = Pay.objects.filter(
            order__user = self.request.user
        ).prefetch_related("order__items")
        items = []
        for pay in pays:
            item = {
                "total_price": pay.total_price,
                "created": pay.created,
                "cart_list": [
                    {
                        "product": cart.product,
                        "total_price": cart.total_item_cost,
                        "quentity": cart.quentity
                    }
                    for cart in pay.order.item_detail
                ]
            }
            items.append(item)
        
        return items


    