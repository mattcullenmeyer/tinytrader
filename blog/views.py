from django.http.response import JsonResponse
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json

from .models import Post, Comment
from users.models import User
from .forms import CommentForm

class BlogListView(ListView):
  queryset = Post.objects.filter(status=1).order_by('-updated_on')
  template_name = 'blog/blog_list.html'

class BlogDraftListView(ListView):
  queryset = Post.objects.filter(status=0).order_by('-updated_on')
  template_name = 'blog/blog_list.html'

def BlogDetailView(request, slug):
  template_name = 'blog/blog_detail.html'
  post = Post.objects.get(slug=slug)
  comments = post.comments.filter(active=True)
  
  if request.method == 'POST':
    data = json.loads(request.body)
    content = data.get('content')

    post = Post.objects.get(id=content['post'])
    name = User.objects.get(id=content['name'])

    comment = Comment(post=post, name=name, body=content['body'])
    comment.save()

    response_data = {
      'newCommentId': comment.id,
      'newCommentName': comment.name.username,
      'newCommentCreatedOn': comment.created_on,
      'newCommentBody': comment.body,
    }

    return JsonResponse(response_data, status=201, safe=False)

  else:
    form = CommentForm()
    
    context = {
      'post': post,
      'comments': comments,
      'form': form,
    }

    return render(request, template_name, context)
