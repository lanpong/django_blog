#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Time : 2018/9/22 10:46
    File : urls.py
    __author__ = 'hdy'
"""
from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/(?P<pk>[0-9]+)/', views.PostDetailView.as_view(), name='detail'),
    path('archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.ArchivesView.as_view(), name='archives'),
    path('category/(?P<pk>[0-9]+)/', views.CategoryView.as_view(), name='category'),
    path('tag/(?P<pk>[0-9]+)/', views.TagView.as_view(), name='tag'),
]