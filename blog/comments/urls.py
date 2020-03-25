from django.conf.urls import url
from .views import *


app_name = "comments"
urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name="index")
]