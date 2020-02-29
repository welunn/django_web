from django.db import models


# 定义UserInfo类，集成models.Model
class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    gender = models.BooleanField(default=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)


    def __str__(self):
        return self.username


# 定义博客类
class BlogInfo(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=512)
    createTime = models.DateTimeField()
    createBy = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

