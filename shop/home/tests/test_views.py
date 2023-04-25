from django.test import TestCase, Client
from django.urls import resolve, reverse



class HomeUrlsTest(TestCase):
    def setUp(self):
        self.home_url = reverse("home:home")
        self.client = Client()

    def test_home_view_status_code(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
