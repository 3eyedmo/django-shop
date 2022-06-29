from django.test import TestCase

from products.models import Category, Product



class ProductModelsTest(TestCase):
    def setUp(self):
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

    def test_product_model(self):
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.name, self.product_name)
        self.assertEqual(self.product.discription, self.product_discription)
        self.assertEqual(self.product.price, self.product_price)
        self.assertEqual(self.product.quentity, self.product_quentity)

    def test_category_model(self):
        self.assertEqual(self.category.name, self.category_name)