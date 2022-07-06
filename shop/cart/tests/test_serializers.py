import json

import pytest
from cart.serializers import CartItemAddOrCreateSerializer
from django.urls import resolve, reverse
from django.middleware.csrf import get_token
from django.test import Client
from cart.views import CartItemAddOrCreateView
from orders.models import Order
from django.core.handlers.wsgi import WSGIRequest

def test_product(created_product):
    assert created_product.name == "Asus"

def test_add_create_serializer(
    get_serializer_context
):
    assert "order" in get_serializer_context
    assert "request" in get_serializer_context
    order = get_serializer_context.get("order")
    request = get_serializer_context.get("request")
    assert isinstance(order, Order)
    assert isinstance(request, WSGIRequest)
    


@pytest.mark.parametrize(
    "quentity, product, validity",
    [
        (1, 1, True),
        (2, 1, False),
        (1, 2, False)
    ]
)
def test_serializer_input(
    db,
    created_product,
    get_serializer_context,
    quentity,
    product,
    validity
):
    serializer = CartItemAddOrCreateSerializer(
        data={
            "product": product,
            "quentity": quentity
        },
        context=get_serializer_context
    )
    assert serializer.is_valid() == validity



    
