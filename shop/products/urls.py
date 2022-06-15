from django.urls import path
from products import views

app_name="products"
urlpatterns = [
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
]