import re
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from requests import session

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



class PasswordGetEmailView(generic.TemplateView):
    template_name: str = "accounts/forget_password/get_email/index.html"


from accounts.utils import send_email
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import smart_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.urls import reverse
from functools import wraps
User = get_user_model()

def get_user_information(func):

    @wraps
    def dec(self, request):
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
        except:
            return func(self, request)
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        token = PasswordResetTokenGenerator().make_token(user)
        current_site = get_current_site(request=request).domain
        url = reverse("accounts:password_verify", kwargs={
            "token": token,
            "uidb64":uidb64
        })
        relative_link = current_site + url
        return func(self, request, email, relative_link, send_email)
    return dec


class PasswordSentEmailView(View):
    template_name: str = "accounts/forget_password/email_sent/index.html"

    @get_user_information
    def post(self, request, email=None, relative_link=None, send_email=None):
        if send_email:
            email_subject = "تغییر پسوورد"
            send_email(email=email, link=relative_link, subject=email_subject)
        return render(request, self.template_name)




def token_validator(func):

    @wraps
    def dec(self, request, *args, **kwargs):
        token = kwargs.get("token")
        uidb64 = kwargs.get("uidb64")
        user_id = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, id=user_id)
        if not PasswordResetTokenGenerator().check_token(user=user, token=token):
            raise Http404
        if request.method == "GET":
            return func(self, request, token, uidb64)
        return func(self, request, user, token, uidb64)
    
    return dec

from accounts.forms import PasswordForgetForm, PasswordChangeForm

class PasswordVerify(View):
    template_name = "accounts/forget_password/verify_password/index.html"
    form = PasswordForgetForm
    http_method_names = [
        "get", "post"
    ]

    @token_validator
    def get(self, request, token, uidb64):
        context = {
            "token": token,
            "uidb64": uidb64
        }
        return render(request, self.template_name, context=context)

    @token_validator
    def post(self, request, user, token, uidb64):
        form = self.form(data=request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data.get("password2"))
            user.save()
            return redirect("accounts:login")

        context = {
            "token": token,
            "uidb64": uidb64
        }
        return render(request, self.template_name, context=context)


class ChangePasswordView(LoginRequiredMixin, View):
    teamplate_name = "accounts/change_password/index.html"
    form = PasswordChangeForm

    def post(self, request):
        user = request.user
        form = self.form(data=request.POST, user=user)
        if form.is_valid():
            user.set_password(form.cleaned_data.get("password2"))
            user.save()
            return redirect("home:home")
        
        return render(request, self.teamplate_name)

    def get(self, request):
        return render(request, self.teamplate_name)


