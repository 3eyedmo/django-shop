import pytest
from pytest_factoryboy import register
from django.test import Client
from .factories import CategoryFactory, ProductFactory, UserFactory
from django.urls import reverse
from cart.views import CartItemAddOrCreateView
from django.contrib.sessions.middleware import SessionMiddleware


register(CategoryFactory)
register(ProductFactory)
register(UserFactory)


@pytest.fixture
def created_product(db, product_factory):
    product = product_factory.create()
    return product


@pytest.fixture
def client_without_csrf():
    client = Client(enforce_csrf_checks=False)


@pytest.fixture
def created_user(db, user_factory):
    user = user_factory.create()
    return user


@pytest.fixture
def add_create_url():
    url = reverse("cart:add_cart")
    return url

@pytest.fixture
def add_or_create_view_class_instance(
    rf,
    created_user,
    add_create_url
):
    rf = rf.post(add_create_url)
    rf.user = created_user
    instance = CartItemAddOrCreateView()
    instance.setup(request=rf)
    return instance


@pytest.fixture
def get_serializer_context(
    db,
    add_or_create_view_class_instance
):
    context = add_or_create_view_class_instance.get_serializer_context()
    return context
