from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField


class RegisterForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = UserProfile
        fields = ['email','password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email','password']