from django.conf.urls import url
from .views import *


app_name = "polls"
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^detail/(\d+)/$', DetailView.as_view(), name="detail"),
    url(r'^result/(\d+)/$', ResultViews.as_view(), name="result"),
    url(r'^zero/$', zero, name="zero"),
    url(r'^login/$', LoginView.as_view(), name="login")
]