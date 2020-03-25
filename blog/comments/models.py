from django.db import models
from article.models import Article


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=30, verbose_name="名称")
    content = models.CharField(max_length=500, verbose_name="评论内容")
    email = models.EmailField(blank=True, null=True, verbose_name="电子邮件")
    url = models.URLField(blank=True, null=True, verbose_name="个人网站")
    create_time = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

