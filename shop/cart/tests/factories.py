import factory
from faker import Faker
from django.contrib.auth import get_user_model
from cart.models import CartItem
from products.models import Product, Category


User = get_user_model()
faker = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Laptop"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "Asus"
    category = factory.SubFactory(CategoryFactory)
    discription = faker.text()
    price = 18_000_000
    quentity = 15
    valid_order_number = 1


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = faker.email()
    password = "123456789Ksj"

    
