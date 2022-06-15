from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import RegisterForm, LoginForm

class LoginView(View):
    http_method_names = [
        'post',
        'get'
    ]
    def get(self, request):
        return render(request, 'accounts/login/login.html')

    def post(self, request):
        data = request.POST
        form = LoginForm(data=data)
        if form.is_valid():
            user = authenticate(
                email = form.cleaned_data.get("email"),
                password = form.cleaned_data.get("password")
            )
            if user is not None:
                print(user)
                login(request, user)
                return redirect("home:home")
            messages.warning(request, "email or password is wrong")

        context = {
            "form": form
        }
        return render(request, 'accounts/login/login.html', context=context)



class RegisterView(View):
    http_method_names = [
        'post',
        'get'
    ]

    def get(self, request):
        return render(request, 'accounts/register/register.html')
    
    def post(self, request):
        data = request.POST
        form = RegisterForm(data=data)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
        context = {
            "form": form
        }
        print(form.errors)
        return render(request, 'accounts/register/register.html', context=context)


class LogoutView(LoginRequiredMixin, View):
    http_method_names = [
        "get"
    ]

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home:home")