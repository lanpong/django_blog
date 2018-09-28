#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Time : 2018/9/28 15:40
    File : search_indexes.py
    __author__ = 'hdy'
"""
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
