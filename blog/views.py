from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Post, Comment

class BlogListView(ListView):
  queryset = Post.objects.filter(status=1).order_by('-updated_on')
  template_name = 'blog/blog_list.html'

class BlogDraftListView(ListView):
  queryset = Post.objects.filter(status=0).order_by('-updated_on')
  template_name = 'blog/blog_list.html'

def BlogDetailView(request, slug):
  post = Post.objects.get(slug=slug)
  comments = post.comments.filter(active=True)
  context = {
    'post': post,
    'comments': comments,
  }
  return render(request, 'blog/blog_detail.html', context)
