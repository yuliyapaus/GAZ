from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.base_user import BaseUserManager

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True)




