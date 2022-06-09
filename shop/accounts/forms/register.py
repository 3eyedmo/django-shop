from django import forms
from django.contrib.auth import get_user_model

from accounts.utils import CheckPassword



User = get_user_model()


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()
    email = forms.EmailField(max_length=255, min_length=5)
    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2"
        )

    def clean_password2(self):
        password2 = self.cleaned_data["password2"]
        password1 = self.cleaned_data["password1"]
        check_password = CheckPassword(password1=password1, password2=password2)
        if not check_password():
            raise forms.ValidationError(check_password.error_message)
        return password2

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email exists")
        return email
    
    
    def save(self, commit=False):
        password = self.cleaned_data["password2"]
        email = self.cleaned_data["email"]
        user = User(email = email, password=password, is_active=True)
        user.save()
        return user


    
    
    
    