import string

from django.conf import settings
from django.core.mail import send_mail

class CheckPassword:
    MIN_PASS_LENGTH = 8
    MAX_PASS_LECGTH = 25
    error_message = None

    def __init__(self, password1, password2):
        self.pass1 = password1
        self.pass2 = password2
    
    def __call__(self):
        if self.equality() and self.check_length():
            return self.check_digit() and self.check_lowwer_case() and self.check_upper_case()
        return False
            

    def check_length(self):
        if not self.MIN_PASS_LENGTH <= len(self.pass2) <= self.MAX_PASS_LECGTH:
            self.error_message = "password must be between 8 and 25!"
            return False
        return True
    
    def equality(self):
        if self.pass1 != self.pass2:
            self.error_message = "passwords not match!"
            return False
        return True

    def check_digit(self):
        digits = string.digits
        if not any(char in digits for char in self.pass2):
            self.error_message = "password must containe digits"
            return False
        return True
    
    def check_lowwer_case(self):
        if self.pass2.upper() == self.pass2:
            self.error_message = "password must have at least one lower case"
            return False
        return True

    def check_upper_case(self):
        if self.pass2.lower() == self.pass2:
            self.error_message = "password must have at least one upper case"
            return False
        return True



def send_email(email, link, subject):
    message = f"you need to click following link {link}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)