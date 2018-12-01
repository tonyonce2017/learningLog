from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .models import *

urlpatterns = [
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'),  name='login'),
    # path('login', LoginView.as_view(template_name='users/login.html'),  name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='main/index.html'),  name='logout'),
    path('register', views.register, name='register'),
]