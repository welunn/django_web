from django.shortcuts import render, redirect, reverse
# from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView
from .models import *
from .forms import *


# 定义用户登录权限校验的装饰器
def checklogin(func):
    def check(self, req, *args):
        # 如果用户登录过，直接继续往下执行
        # if req.COOKIES.get("username"):
        #     return func(self, req, *args)
        if req.session.get("username"):
            return func(self, req, *args)
        else:
            # 如果用户未登录过，跳转到登录页面
            return redirect(reverse("polls:login"))
    return check


# 采用视图类的方式
class IndexView(ListView):


    @checklogin
    def get(self, request):

        # username = request.COOKIES.get('username')
        # if username:
        #     # 查询所有的问题信息
        #     questions = Question.objects.all()
        #     return render(request, "polls/index.html", {"questions": questions})
        # else:
        #     return redirect(reverse("polls:login"))

        questions = Question.objects.all()
        name = "welun--王振伟"
        info = "<h2><a href='http://www.baidu.com'>百度一下</a></h2>"
        return render(request, "polls/index.html", locals())


# 采用视图类的方式实现
class DetailView(DetailView):


    @checklogin
    def get(self, request, id):
        # 从cookie中获取用户信息，判断是否登录了，如果没有登录返回登录页面
        # username = request.COOKIES.get("username")
        # if username:
        #     question = Question.objects.all().get(pk=id)
        #     return render(request, "polls/detail.html", locals())
        # else:
        #     return redirect(reverse("polls:login"))
        question = Question.objects.all().get(pk=id)
        return render(request, "polls/detail.html", locals())


    def post(self, request, id):
        # 获取投票选项的id
        c_id = request.POST.get("info")
        choice = Choice.objects.get(pk=c_id)
        choice.polls += 1
        choice.save()

        return redirect(reverse("polls:result", args=(id, )))


class ResultViews(View):
    def get(self, request, id):
        question = Question.objects.all().get(pk=id)
        return render(request, "polls/result.html", locals())


# 内容部服务器错误方法
def zero(request):
    result = 10 / 0
    return render(request, "polls/index.html")


# 用户登录类
class LoginView(View):


    def get(self, req):
        fm = MyForms()
        print(fm)
        return render(req, "polls/login.html", locals())


    def post(self, req):
        username = req.POST['username']
        password = req.POST['password']

        # res = redirect(reverse("polls:index"))
        # 使用cookie存储
        # from datetime import datetime, timedelta
        # # cookie中保存七天
        # res.set_cookie("username", username, expires=datetime.now() + timedelta(days=7))
        # return res
        # 使用session的方式存储
        req.session["username"] = username
        # 通过form对象获取用户提交的信息
        fm = MyForms(req.POST)
        print(fm)
        username = fm.cleaned_data["username"]
        password = fm.cleaned_data["password"]
        email = fm.cleaned_data["email"]
        print(username, email, password)
        return redirect(reverse("polls:index"))
