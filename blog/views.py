from django.shortcuts import render, get_object_or_404
import markdown
from markdown.extensions.toc import TocExtension
from django.db.models import Q
from django.views.generic import ListView, DeleteView
