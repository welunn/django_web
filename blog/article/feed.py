from django.contrib.syndication.views import Feed
from .models import Article


class ArticleFeed(Feed):
    title = "python学习博客"
    description = "给大家介绍一些python django的开发知识"
    link = "/"


    def items(self):
        articles = Article.objects.all().order_by("-create_time")[:3]
        return articles


    def item_title(self, item):
        return item.title


    def item_description(self, item):
        return item.body[:128]


    def item_link(self, item):
        return "/single%s"%(item.id,)


