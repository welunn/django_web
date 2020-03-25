from django.conf.urls import url
from .views import *
from .feed import ArticleFeed


app_name = "article"
urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^single/(\d+)/$', SingeView.as_view(), name="single"),
    url(r'^articles/(\d+)/(\d+)/$', ArticleView.as_view(), name="articles"),
    url(r'^category/(\d+)/$', CategoryView.as_view(), name="category"),
    url(r'^tag/(\d+)/$', TagView.as_view(), name="tag"),
    url(r'^rss/$', ArticleFeed(), name="rss"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
    url(r'^sendmail/$', SendMailView.as_view(), name="sendmail"),
    url(r'^active/(.*?)/$', ActiveView.as_view(), name="active"),
]

