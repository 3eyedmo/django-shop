from django.urls import path
from cart import views

app_name="cart"
urlpatterns = [
    path("add/", views.CreateCartItem.as_view(), name="add_cart"),
    path("list/", views.ListCartItems.as_view(), name="cartlist"),
    path("<int:pk>/", views.RetrieveUpdateDestroyCartItem.as_view(), name="retrieve_update_delete")
]
