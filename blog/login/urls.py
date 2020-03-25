from django.conf.urls import url
from .views import *


app_name = "user"
urlpatterns = [
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^index/$', IndexView.as_view(), name="index"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^checkname/$', CheckView.as_view(), name="checkname"),
    url(r'^verify/$', VerifyView.as_view(), name="verify"),
]