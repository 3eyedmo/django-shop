from django.urls import path
from .views import home, test


app_name = "home"
urlpatterns = [
    path('', home, name='home'),
    path('test/', test, name='test'),
]
