from django.conf.urls import url
from django.urls import path
# 导入视图文件
from .views import index, list, detail, delete, deleteblog, adduser,addblog


# 定义项目名称
app_name = "blog"


urlpatterns = [
    url(r"^$", index, name="index"),
    # 用户管理
    url(r"^list/$", list, name="list"),
    url(r"^detail/(\d+)/$", detail, name="detail"),
    url(r"^delete/(\d+)/$", delete, name="delete"),
    url(r"^adduser/$", adduser, name="adduser"),
    # 博客管理
    url(r"^addblog/(\d+)/$", addblog, name="addblog"),
    # 删除博客
    url(r"^deleteblog/(\d+)\$", deleteblog, name="deleteblog")
]


