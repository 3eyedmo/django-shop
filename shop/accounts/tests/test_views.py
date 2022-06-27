from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

User = get_user_model()


class LoginViewTest(TestCase):
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

    def test_login_GET(self):
        response = self.client.get(path=self.login_url)
        self.assertEqual(response.status_code, 200)

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
        


class RegisterViewTest(TestCase):
    """
    This test examine the register view responses.
    """
    def setUp(self):
        self.user1 = {
            "email":"armin403000@yahoo.com",
            "password1":"13sad5436wadM",
            "password2":"13sad5436wadM"
        }
        self.user2 = {
            "email":"armin403000@yahoo.com",
            "password1":"13sad5436wadM",
            "password2":"13sad5436wad"
        }
        self.register_url = reverse("accounts:register")
        self.client = Client()

    def test_register_GET(self):
        url = self.register_url
        response = self.client.get(
            path=url
        )
        self.assertEqual(response.status_code, 200)

    def test_register_proper_POST(self):
        url = self.register_url
        response = self.client.post(
            path=url,
            data=self.user1
        )
        self.assertEqual(response.status_code, 302)
    
    def test_register_wrong_POST(self):
        url = self.register_url
        response = self.client.post(
            path=url,
            data=self.user2
        )
        self.assertEqual(response.status_code, 200)



class LogoutViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="customer@customer.com",
            password="customer123"
        )
        self.client = Client()
        self.url = reverse("accounts:logout")

    def test_logout(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, 302)



class PasswordForgetSendEmailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="customer@customer.com",
            password="customer123"
        )
        self.client = Client()
        self.url = reverse("accounts:password_forget_send_email")

    def test_view_POST(self):
        data = {
            "email": self.user.email
        }
        response = self.client.post(
            path=self.url
        )
        self.assertEqual(response.status_code, 200)


class PasswordForgetGetEmailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("accounts:password_forget_get_email")

    def test_view_GET(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)







class PasswordVerifyViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="customer@customer.com",
            password="customer123"
        )

        self.token = PasswordResetTokenGenerator().make_token(self.user)
        self.uidb64 = urlsafe_base64_encode(smart_bytes(self.user.id))
        self.client = Client()
        self.url = reverse(
            "accounts:password_verify",
            args=(self.token, self.uidb64)
        )

    def test_view_GET(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_view_POST(self):
        data = {
            "password1": "13741374Mh",
            "password2": "13741374Mh"
        }
        response = self.client.post(
            path=self.url,
            data=data
        )
        self.assertEqual(response.status_code, 302)



class ChangePasswordView(TestCase):
    def setUp(self):
        self.password = "customer123"
        self.email = "customer@customer.com"
        self.user = User.objects.create_user(
            email=self.email,
            password=self.password
        )
        self.client = Client()
        self.url = reverse("accounts:change_password")

    def test_proper_reset_password(self):
        data = {
            "old_password": self.password,
            "password1": "13741374mH",
            "password2": "13741374mH"
        }
        response = self.client.post(
            path=self.url,
            data=data
        )
        self.assertEqual(response.status_code, 302)
