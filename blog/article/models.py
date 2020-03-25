from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Tags(models.Model):
    """
    标签表：
    title: 标签标题
    标签与文章： 多对多的关系
    """
    title = models.CharField(max_length=30)


    def __str__(self):
        return self.title


class Category(models.Model):
    """
    分类表：
    title: 分类标题
    与文章表的关系：一对多
    """
    title = models.CharField(max_length=30)


    def __str__(self):
        return self.title


class Article(models.Model):
    """
    文章表： 标签表：多对多， 分类表： 一对多
    """
    title = models.CharField(max_length=30)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)


    def __str__(self):
        return self.title


# 轮播图 实体类
class Ads(models.Model):
    pic = models.ImageField(upload_to='ads')
    desc = models.CharField(max_length=20)
    url = models.CharField(max_length=20)


    def __str__(self):
        return self.desc


# 富文本编辑器 实体类
class MessageInfo(models.Model):
    username = models.CharField(max_length=20, blank=True, null=None)
    email = models.CharField(max_length=20, blank=True, null=None)
    subject = models.CharField(max_length=20, blank=True, null=None)
    message = HTMLField()


    def __str__(self):
        return self.email

