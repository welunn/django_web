from django import forms


class MyForms(forms.Form):
    username = forms.CharField(label="用户名", max_length=10, min_length=4, widget=forms.TextInput(attrs={"id": "username", "class": "form-control"}))
    password = forms.CharField(label="密码", max_length=20, min_length=6, widget=forms.PasswordInput(attrs={"id": "password", "class": "form-control"}))
    email = forms.CharField(label="电子邮件", widget=forms.EmailInput(attrs={"id": "email", "class": "form-control"}))

