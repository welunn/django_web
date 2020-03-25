from django.template import Library
from ..models import Article, Category, Tags, Ads


register = Library()


# 获取最新文章
@register.simple_tag
def getlatestarticles(num=3):
    """
    获取最新文章列表，根据创建时间create_time排序
    :param num:
    :return:
    """
    latestarticles = Article.objects.all().order_by("-create_time")[:num]
    return latestarticles


# 获取归档信息
@register.simple_tag
def getarticled(num=3):
    """
    create_time: 要处理的字段
    month： 过滤重复的字段
    :param num:
    :return:
    """
    result = Article.objects.dates("create_time", "month")
    print(result)
    return result


@register.simple_tag
def getcategorys():
    """
    获取所有的分类列表
    :return:
    """
    categorys = Category.objects.all()
    return categorys


@register.simple_tag
def gettags():
    """
    获取所有文章标签
    :return:
    """
    return Tags.objects.all()


@register.simple_tag
def getads():
    """
    获取所有的轮播图片信息
    :return:
    """
    return Ads.objects.all()

