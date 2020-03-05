from django import forms
from .models import MyUser
from django.utils.translation import gettext_lazy


class LoginForm(forms.ModelForm):
    """
    生成模型表单
    """
    class Meta():
        model = MyUser
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }
        help_texts = {
            "username": gettext_lazy("")
        }



class RegisterForm(forms.ModelForm):
    """
    生成模型表单
    """
    class Meta():
        model = MyUser
        fields = ["username", "password", "email", "telephone"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telephone": forms.TextInput(attrs={"class": "form-control"})
        }
        help_texts = {
            "username": gettext_lazy("")
        }
        labels = {
            "telephone": "电话号码"
        }