#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Time : 2018/9/20 22:09
    File : urls.py
    __author__ = 'hdy'
"""
from django.urls import path, re_path
from . import views

app_name = 'comments'
urlpatterns = [
    re_path('comment/post/(?P<post_pk>[0-9]+)/', views.post_comment, name='post_comment'),
]
