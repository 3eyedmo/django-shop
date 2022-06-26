from django.urls import path
from . import views


app_name="accounts"
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('password_forget/get_email/', views.PasswordGetEmailView.as_view(), name="password_forget_get_email"),
    path('password_forget/send_email/', views.PasswordSentEmailView.as_view(), name="password_forget_send_email"),
    path('password_forget/<str:token>/<str:uidb64>/', views.PasswordVerify.as_view(), name="password_verify"),
    path('change_password/', views.ChangePasswordView.as_view(), name="change_password")
]
