from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.forms import (
    LoginForm,
    RegisterForm,
    PasswordForgetForm,
    PasswordChangeForm
)


User = get_user_model()


class LoginFormTest(TestCase):
    """
    This test evaluate Login Form.
    """
    def setUp(self):
        self.user_email = "customer@customer.com"
        self.user_password = "customer_password"
        self.user = User.objects.create_user(
            email=self.user_email,
            password=self.user_password
        )

    def test_valid_information(self):
        data = {
            "email":self.user_email,
            "password":self.user_password
        }
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_information(self):
        data = {
            "email":self.user_email
        }
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())

class RegisterFormTest(TestCase):
    """
    This test evaluate register Form.
    """
    def setUp(self):
        self.user_email = "customer@customer.com"
        self.user_password = "customer_password123M"
        self.user = User.objects.create_user(
            email=self.user_email,
            password=self.user_password
        )

    def test_valid_information(self):
        data = {
            "email":"customer@different.com",
            "password1":self.user_password,
            "password2":self.user_password
        }
        form = RegisterForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_information(self):
        data = {
            "email":self.user_email,
            "password1":self.user_password,
            "password2":self.user_password
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())



class ChangePasswordFormTest(TestCase):
    """
    This test evaluate Change Password Form.
    """
    def setUp(self):
        self.user_email = "customer@customer.com"
        self.user_password = "customer_password123M"
        self.user = User.objects.create_user(
            email=self.user_email,
            password=self.user_password
        )
    
    def test_valid_information(self):
        data = {
            "old_password":self.user_password,
            "password1": "123456789mH",
            "password2": "123456789mH",
        }
        form = PasswordChangeForm(
            data=data,
            user=self.user
        )
        self.assertTrue(form.is_valid())

    def test_invalid_information(self):
        data = {
            "old_password":"123456789mH",
            "password1": "123456789mH",
            "password2": "123456789mH",
        }
        form = PasswordChangeForm(
            data=data,
            user=self.user
        )
        self.assertFalse(form.is_valid())



class ForgetPasswordFormTest(TestCase):
    """
    This test evaluate Forget PasswordForm.
    """
    def setUp(self):
        self.user_email = "customer@customer.com"
        self.user_password = "customer_password123M"
        self.user = User.objects.create_user(
            email=self.user_email,
            password=self.user_password
        )

    def test_valid_data(self):
        data = {
            "password1": "13546msandjK",
            "password2": "13546msandjK"
        }
        form = PasswordForgetForm(data=data)
        self.assertTrue(form.is_valid())