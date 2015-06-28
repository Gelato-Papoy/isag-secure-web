# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login),
    # url(r'^login_check/$', views.login_check),
]