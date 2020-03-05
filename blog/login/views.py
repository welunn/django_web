from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import *
from django.contrib.auth import authenticate, login, logout


# 检查用户是否登录的装饰器函数
def checklogin(func):
    def check(self, request):

        if request.user and request.user.is_authenticated:
            return func(self, request)
        else:
            return redirect(reverse("user:login"))
    return check



class IndexView(View):
    @checklogin
    def get(self, request):
        return render(request, "user/index.html", locals())


class LoginView(View):
    def get(self, request):
        lf = LoginForm()
        rf = RegisterForm()
        return render(request, "user/login-register.html", locals())


    def post(self, request):
        # 获取用户输入的信息
        username = request.POST["username"]
        password = request.POST["password"]

        # user = MyUser.objects.get(username=username, password=password)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, "user/index.html")
        else:
            errorMessage = "登录失败！"
            lf = LoginForm()
            rf = RegisterForm()
            return render(request, "user/login-register.html", locals())


class RegisterView(View):
    def get(self, request):
        return render(request, "user/login-register.html", locals())


    def post(self, request):
        try:
            rf = RegisterForm(request.POST)
            print(rf)
            username = rf.cleaned_data["username"]
            password = rf.cleaned_data["password"]
            email = rf.cleaned_data["email"]
            telephone = rf.cleaned_data["telephone"]

            # print(rf.username, rf.password, rf.email, rf.telephone)
            # username = request.POST.get("username")
            # password = request.POST.get("password")
            # email = request.POST.get("email")
            # telephone = request.POST.get("telephone")
            # print(username, password)

            # myUser = MyUser(username=username, password=password, email=email, telephone=telephone)
            # myUser.save()
            user = MyUser.objects.create_user(username=username, password=password, email=email, telephone=telephone)
            if user:
                return redirect(reverse("user:index"))
        except:
            errorMessage = "注册失败"
            lf = LoginForm()
            rf = RegisterForm()
            return render(request, "user/login-register.html", locals())


# 用户退出类
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("user:login"))