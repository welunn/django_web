from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse


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
        verify = request.POST["verify"]
        print(verify)
        verifycode = request.session["verifycode"]
        if verify != verifycode:
            errorMessage = "验证码错误！"
            lf = LoginForm()
            rf = RegisterForm()
            return render(request, "user/login-register.html", locals())
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


# 检查用户名是否存在
class CheckView(View):
    def get(self, request):
        username = request.GET["username"]
        user = MyUser.objects.filter(username=username)
        print(username)
        print(user)
        if user:
            json = JsonResponse({"statecode": 0, "msg": "用户名可以使用"})
            return json
        else:
            json = JsonResponse({"statecode": 1, "msg": "用户名不存在,请重新输入！"})
            return json


# 验证码实现
import random, io
from PIL import Image, ImageDraw, ImageFont
class VerifyView(View):
    def get(self, request):
        # 定义变量，用于画面的背景色、宽、高
        bgcolor = (random.randrange(20, 100),
                   random.randrange(20, 100),
                   random.randrange(20, 100))
        width = 100
        heigth = 25
        # 创建画面对象
        im = Image.new('RGB', (width, heigth), bgcolor)
        # 创建画笔对象
        draw = ImageDraw.Draw(im)
        # 调用画笔的point()函数绘制噪点
        for i in range(0, 100):
            xy = (random.randrange(0, width), random.randrange(0, heigth))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
        # 定义验证码的备选值
        str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
        # 随机选取4个值作为验证码
        rand_str = ''
        for i in range(0, 4):
            rand_str += str1[random.randrange(0, len(str1))]
        # 构造字体对象
        font = ImageFont.truetype('SitkaB.ttc', 23)
        fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
        # 绘制4个字
        draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
        draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
        draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
        draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
        # 释放画笔
        del draw
        request.session['verifycode'] = rand_str
        f = io.BytesIO()
        im.save(f, 'png')
        # 将内存中的图片数据返回给客户端，MIME类型为图片png
        return HttpResponse(f.getvalue(), 'image/png')
