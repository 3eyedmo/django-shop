from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve


User = get_user_model()



class BaseViewTest(TestCase):
    """
    This Test Class tests if a view get a proper response.
    """

    def setUp(self):
        self.user_pass = "customer_password"
        self.user_email = "customer@customer.com"
        self.user = User.objects.create_user(
            email=self.user_email,
            password=self.user_pass
        )
        self.client = Client()

        self.login_url = reverse("accounts:login")
        self.register_url = reverse("accounts:register")



class LoginViewTest(BaseViewTest):

    def test_login_GET(self):
        response = self.client.get(path=self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 300)
        self.assertNotEqual(response.status_code, 400)

    def test_login_POST(self):
        data = {
            "email":self.user_email,
            "password":self.user_pass
        }
        response = self.client.post(
            path=self.login_url,
            data=data
        )
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(response.status_code, 300)
        self.assertNotEqual(response.status_code, 400)
        self.assertNotEqual(response.status_code, 200)


    


        
