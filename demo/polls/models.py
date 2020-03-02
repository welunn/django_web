from django.db import models
"""
用户投票程序：
1.数据库表设计：
    问题表：主要用于记录真对投票的问题（主表)
        字段：标题，创建时间
    选项表：真对每个问题都有几个选项(子表)
        字段：选项标题，票数，外键（request)
"""


# 定义问题model类
class Question(models.Model):
    title = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


# 选项表
class Choice(models.Model):
    title = models.CharField(max_length=50)
    polls = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
