from django.test import TestCase
from django.urls import resolve, reverse

from home.views import HomeView


class HomeUrlsTest(TestCase):
    def setUp(self):
        self.home_url = reverse("home:home")

    def test_home_products(self):
        self.assertEqual(resolve(self.home_url).func.view_class, HomeView)
