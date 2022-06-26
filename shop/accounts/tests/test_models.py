from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTest(TestCase):
    def setUp(self):
        self.customer_email = "customer@customer.com"
        self.customer_password = "customerPassword123!@#"
        self.admin_email = "admin@admin.com"
        self.admin_password = "adminPassword123!@#"
        self.customer = User.objects.create_user(
            email=self.customer_email,
            password=self.customer_password
        )
        self.admin = User.objects.create_superuser(
            email=self.admin_email,
            password=self.admin_password
        )

    def test_activity(self):
        self.assertTrue(self.customer.is_active)
        self.assertTrue(self.admin.is_active)
    
    def test_admin(self):
        self.assertTrue(self.admin.is_admin)
        self.assertFalse(self.customer.is_admin)

    def test_customer_email(self):
        self.assertEqual(self.customer.email, self.customer_email)

    def test_admin_email(self):
        self.assertEqual(self.admin.email, self.admin_email)

