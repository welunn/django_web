from django.contrib import admin
from .models import UserInfo, BlogInfo


# Register your models here.
# 定义inlines 关联，在添加用户的时候同时可以添加一条博客
class BlogInfoInline(admin.StackedInline):
    # 关联的子表
    model = BlogInfo
    # 关联的个数
    extra = 1


# 重写后台管理功能
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["username", "password", "gender", "age", "phone"]
    list_filter = ("username", "phone")
    search_fields = ("username",)
    list_per_page = 2
    inlines = [BlogInfoInline]


# 注册实体类
admin.site.register(UserInfo, UserInfoAdmin)


# 定义博客后台管理类
class BlogInfoAdmin(admin.ModelAdmin):
    # 定义显示的字段
    list_display = ("title", "content", "createTime", "createBy")
    # 定义过滤字段
    list_filter = ["title", "createBy"]
    # 定义模糊查询阶段
    search_fields = ("title",)
    # 定义每页显示条数
    list_per_page = 2


# 注册博客模型类
admin.site.register(BlogInfo, BlogInfoAdmin)
