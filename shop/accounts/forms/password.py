from django import forms

from accounts.utils import CheckPassword

class PasswordForgetForm(forms.Form):
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean(self):
        data = super().clean()
        password1 = data.get("password1")
        password2 = data.get("password2")
        pass_validator = CheckPassword(
            password1=password1,
            password2=password2
        )
        if not pass_validator():
            raise forms.ValidationError(pass_validator.error_message)
        return data



class PasswordChangeForm(forms.Form):

    def __init__(self, user=None, *args, **kwargs):
        if not user:
            raise forms.ValidationError("user is None")
        self.user = user
        super().__init__(*args, **kwargs)

    old_password = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    def clean(self):
        data = super().clean()
        password1 = data.get("password1")
        password2 = data.get("password2")
        old_password = data.get("old_password")
        
        if not self.user.check_password(old_password):
            raise forms.ValidationError("last password is wrong")
        pass_validator = CheckPassword(
            password1=password1,
            password2=password2
        )
        if not pass_validator():
            raise forms.ValidationError(pass_validator.error_message)
        return data

    