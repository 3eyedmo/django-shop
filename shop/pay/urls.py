from django.urls import path
from . import views


app_name="pay"
urlpatterns = [
    path("verify/", views.VerifyPay.as_view(), name="verify_pay"),
    path("complete/", views.CompletePay.as_view(), name="complete_pay"),
    path("pay_list/", views.ListPays.as_view(), name="pay_list"),

]
