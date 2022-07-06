from django.views import generic
from django.db.models import Q
import django_filters

from products.models import Category, Product



class ProductFilterset(django_filters.FilterSet):
    """
    This module filters a queryset based on category, price(from, to) and a key word.
    """
    category__id = django_filters.NumberFilter(lookup_expr='iexact')
    category__name = django_filters.CharFilter(lookup_expr='iexact')
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    search = django_filters.CharFilter(method="search_key")
    class Meta:
        model = Product
        fields = [
            'category',
            'price',
        ]
    def search_key(self, query_set, name, value):
        q1 = Q(name__contains = value)
        q2 = Q(discription__contains = value)
        q3 = Q(category__name__contains = value)
        qs = query_set.filter(
            q1 | q2 | q3
        )
        return qs
    


class HomeView(generic.ListView):
    """
    This view gives all products based on a filter.
    """
    model = Product
    template_name: str = "home/index.html"
    paginate_by: int = 2
    page_kwarg: str = "page"


    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        f = ProductFilterset(self.request.GET, queryset=qs)
        return f.qs.order_by("-created")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({
            "cats": Category.objects.all()
        })
        context_data.update({
            "params": self.get_params()
        })
        return context_data

    def get_params(self):
        params_query_dict = self.request.GET
        params_list = [param for param in params_query_dict if param != self.page_kwarg]
        params_string = "?"
        for param in params_list:
            param_value = params_query_dict.getlist(param)[0]
            params_string += f"{param}={param_value}&"
        return params_string
