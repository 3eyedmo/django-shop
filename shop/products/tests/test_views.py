from django.test import TestCase, Client
from django.urls import resolve, reverse

from products.views import ProductDetailView
from products.models import Product, Category


class ProductDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category_name = "Laptop"
        self.category = Category.objects.create(
            name = self.category_name
        )
        self.product_discription = "There is some discription"
        self.product_name = "Asus - A550LD"
        self.product_price = 5000
        self.product_quentity = 45
        self.product = Product.objects.create(
            category = self.category,
            name = self.product_name,
            discription = self.product_discription,
            price = self.product_price,
            quentity = self.product_quentity
        )
        self.product_detail_url_valid = reverse(
            "products:product_detail",
            args=(self.product.id,)
        )
        self.product_detail_url_invalid = reverse(
            "products:product_detail",
            args=(50,)
        )

    def test_valid_data(self):
        response = self.client.get(self.product_detail_url_valid)
        self.assertEqual(response.status_code, 200)

    def test_invalid_data(self):
        response = self.client.get(self.product_detail_url_invalid)
        self.assertEqual(response.status_code, 404)



        