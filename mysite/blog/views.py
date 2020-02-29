from django.shortcuts import render
from django.http import HttpResponse
from .models import UserInfo, BlogInfo
from django.template import loader


# 定义视图 index方法
def index(request):
    blogs = BlogInfo.objects.all()
    print(blogs)
    # 加载模板
    temp = loader.get_template("blog/index.html")
    # 使用模板 渲染动态数据
    res = temp.render({"username": "管理员"})
    # 把渲染结果返回也
    return HttpResponse(res)


# 获取用户列表
def list(request):
    # 获取所有的用户信息
    users = UserInfo.objects.all()
    # 加载模板
    temp = loader.get_template("blog/list.html")
    # 获取动态数据，渲染到静态页面
    res = temp.render({"users": users})
    # 把渲染的动态数据返回页面
    return HttpResponse(res)


# 用户详细页面
def detail(request, id):
    print("这是传递的参数：%s"%(id,))
    userInfo = UserInfo.objects.get(pk=id)
    # 获取模板
    temp = loader.get_template("blog/detail.html")
    # 渲染数据
    res = temp.render({"user": userInfo})
    # 返回页面
    return HttpResponse(res)


# 根据id删除用户信息
def delete(request, id):
    userInfo = UserInfo.objects.get(pk=id)
    userInfo.delete()

    return list(request)