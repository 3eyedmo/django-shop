from django.test import TestCase, Client
from django.urls import resolve, reverse


from products.models import Category, Product
from products.views import ProductDetailView


class ProductsUrlsTest(TestCase):
    def setUp(self):
        self.product_id = 5
        self.product_detail_url = reverse('products:product_detail', args=(self.product_id, ))
        self.client = Client()

    def test_url_view_match(self):
        self.assertEqual(resolve(self.product_detail_url).func.view_class, ProductDetailView)
