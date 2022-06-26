from django.urls import path
from .views import home, test, HomeView


app_name = "home"
urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
