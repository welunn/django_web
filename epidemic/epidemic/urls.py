
from django.contrib import admin
from django.urls import path
from . import views

"""
    urlpatterns 用来存储项目的路由信息 
   
    path(router, view , kwargs , name)
   
    router : 用来定义路由地址
    
    view : 是用来定义视图的，进行业务逻辑处理的代码, 视图函数,
    
    kwargs : 用来给视图 view 传递额外的数据 （一般不常用）
    
    name : 用来给路由设置名字 

"""


urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', views.index, name="index"),

    path('add/', views.add, name="add"),

    path('epidemic/', views.epidemic, name="epidemic"),

    path('add_epidemic/', views.add_epidemic, name="add_epidemic")
]
