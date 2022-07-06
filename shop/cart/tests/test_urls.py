from django.test import TestCase
from django.urls import resolve, reverse

from cart import views



class CartUrlsTest(TestCase):
    def setUp(self):
        self.add_carts_url = reverse("cart:add_cart")
        self.list_carts_url = reverse("cart:cartlist")
        self.retrieve_update_delete_carts = reverse("cart:retrieve_update_delete", args=(1,))

    def test_url_view_func(self):
        self.assertEqual(
            resolve(self.add_carts_url).func.view_class,
            views.CartItemAddOrCreateView
        )
        self.assertEqual(
            resolve(self.list_carts_url).func.view_class,
            views.ListCartItems
        )
        self.assertEqual(
            resolve(self.retrieve_update_delete_carts).func.view_class,
            views.RetrieveUpdateDestroyCartItem
        )
