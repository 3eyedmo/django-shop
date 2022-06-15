from django.shortcuts import render
from products.models import Product
from django.views import generic


class ProductDetailView(generic.DetailView):
    template_name: str = "products/detail/product_detail.html"
    model = Product
    queryset = Product.objects.all()
