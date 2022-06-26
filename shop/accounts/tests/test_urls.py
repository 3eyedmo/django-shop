from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts import views



class TestUrls(SimpleTestCase):
    """
    This Test Class is to test that a certain url belongs to a function
    """

    def setUp(self):
        self.token = "This is a fake token."
        self.uidb64 = "This is a fake uuidb64"

    def test_login_url(self):
        url = reverse("accounts:login")
        self.assertEqual(resolve(url).func.view_class, views.LoginView)

    def test_register_url(self):
        url = reverse("accounts:register")
        self.assertEqual(resolve(url).func.view_class, views.RegisterView)

    def test_logout_url(self):
        url = reverse("accounts:logout")
        self.assertEqual(resolve(url).func.view_class, views.LogoutView)

    def test_forget_get_email_url(self):
        url = reverse("accounts:password_forget_get_email")
        self.assertEqual(resolve(url).func.view_class, views.PasswordGetEmailView)

    def test_password_forget_send_email_url(self):
        url = reverse("accounts:password_forget_send_email")
        self.assertEqual(resolve(url).func.view_class, views.PasswordSentEmailView)

    def test_password_verify_url(self):
        url = reverse("accounts:password_verify", args=(self.token, self.uidb64))
        self.assertEqual(resolve(url).func.view_class, views.PasswordVerify)

    def test_change_password_verify_url(self):
        url = reverse("accounts:change_password")
        self.assertEqual(resolve(url).func.view_class, views.ChangePasswordView)