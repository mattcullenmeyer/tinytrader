from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Post

class BlogListView(ListView):
  queryset = Post.objects.filter(status=1).order_by('-updated_on')
  template_name = 'blog/blog_list.html'

class BlogDraftListView(ListView):
  queryset = Post.objects.filter(status=0).order_by('-updated_on')
  template_name = 'blog/blog_list.html'

class BlogDetailView(DetailView):
  model = Post
  template_name = 'blog/blog_detail.html'
