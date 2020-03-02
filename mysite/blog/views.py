import datetime
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserInfo, BlogInfo
from django.template import loader


# 定义视图 index方法
def index(request):
    # blogs = BlogInfo.objects.all()
    # print(blogs)
    # # 加载模板
    # temp = loader.get_template("blog/index.html")
    # # 使用模板 渲染动态数据
    # res = temp.render({"username": "管理员"})
    # # 把渲染结果返回也
    # return HttpResponse(res)
    return render(request, "blog/index.html", {"username": "管理员"})


# 获取用户列表
def list(request):
    # 获取所有的用户信息
    users = UserInfo.objects.all()
    # 加载模板
    # temp = loader.get_template("blog/list.html")
    # # 获取动态数据，渲染到静态页面
    # res = temp.render({"users": users})
    # # 把渲染的动态数据返回页面
    # return HttpResponse(res)
    return render(request, "blog/list.html", {"users": users})


# 添加用户
def adduser(request):
    # 如果是get请求跳转到用户注册页面
    if request.method == "GET":
        return render(request, "blog/adduser.html")
    # 如果是post请求，把用户注册的信息提交到数据库，并且返回到列表页面
    elif request.method == "POST":
        userInfo = UserInfo()
        userInfo.username = request.POST.get("username")
        userInfo.password = request.POST.get("password")
        userInfo.gender = request.POST.get("gender")
        userInfo.age = request.POST.get("age")
        userInfo.phone = request.POST.get("phone")
        userInfo.save()
        # return HttpResponseRedirect("/list")
        return redirect(reverse("blog:list"))


# 用户详细页面
def detail(request, id):
    print("这是传递的参数：%s"%(id,))
    userInfo = UserInfo.objects.get(pk=id)
    # 获取模板
    # temp = loader.get_template("blog/detail.html")
    # # 渲染数据
    # res = temp.render({"user": userInfo})
    # # 返回页面
    # return HttpResponse(res)
    return render(request, "blog/detail.html", {"user": userInfo})


# 根据id删除用户信息
def delete(request, id):
    userInfo = UserInfo.objects.get(pk=id)
    userInfo.delete()

    # return HttpResponseRedirect("/list/")
    return redirect(reverse("blog:list"))


# 添加博客
def addblog(request, id):
    # 获取用户信息
    userInfo = UserInfo.objects.get(pk=id)
    if request.method == "GET":
        # 跳转到博客添加页面
        return render(request, "blog/addblog.html", {"user": userInfo})
    elif request.method == "POST":
        # 获取博客信息
        blog = BlogInfo()
        blog.title = request.POST.get("title")
        blog.content = request.POST.get("content")
        blog.createTime = datetime.datetime.now()
        blog.createBy = userInfo
        # 把博客信息保存到数据库
        blog.save()
        # 重定向到用户详细及博客列表显示页面
        # return HttpResponseRedirect("/detail/%s"%(id))
        return redirect(reverse("blog:detail", args=(id,)))


# 删除博客信息
def deleteblog(request, id):
    blog = BlogInfo.objects.get(pk=id)
    blog.delete()
    # return HttpResponseRedirect("/detail/%s"%(blog.createBy.id))
    return redirect(reverse("blog:detail", args=(blog.createBy.id,)))
