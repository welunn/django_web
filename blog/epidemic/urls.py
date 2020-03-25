from django.conf.urls import url
from .views import IndexView

app_name = "epidemic"
urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name="index")
]