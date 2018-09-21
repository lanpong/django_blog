#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Time : 2018/9/20 22:02
    File : forms.py
    __author__ = 'hdy'
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
