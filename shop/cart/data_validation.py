from dataclasses import dataclass

from django.utils.translation import gettext_lazy as _
from django.db.models import F


from products.models import Product
from cart.models import CartItem
from cart.models import Order, OrderStatus

@dataclass(frozen=False)
class CartItemDataClass:
    product_id: int
    quentity: int = 1
    error_message: str = ''
    error: bool = False
    max_quentity: int = 10
    product: Product = None

    def is_valid(self):
        for field in self.__dataclass_fields__:
            validate_method = getattr(self, f"is_valid_{field}", None)
            if validate_method:
                validate_method()
       
        if self.error:
            return False
        return True
    

    def is_valid_product_id(self):
        id = self.product_id = int(self.product_id)
        existence = Product.objects.filter(id=id).exists()
        if not existence:
            self.error = True
            self.error_message = _("pdoduct doesn'texists")

        try:
            product = Product.objects.get(id=id)
            self.product = product
        except:
            self.error = True
            self.error_message = _("pdoduct doesn'texists")
        
    

    def is_valid_quentity(self):
        quentity = self.quentity = int(self.quentity)
        if quentity > self.max_quentity:
            self.error = True
            self.error_message = _("invalid quentity")

    def save(self, user):
        order, _ = Order.objects.get_or_create({
            "user":user,
            "status":OrderStatus.Pending
        })
        if CartItem.objects.for_user(user).filter(product=self.product_id).exists():
            cart = CartItem.objects.for_user(user).get(product=self.product_id)
            cart.quentity = F('quentity') + self.quentity
            cart.save()
            return cart
                

        cart = CartItem(
            order=order,
            product=self.product,
            quentity=self.quentity
        )
        cart.save()
        return cart