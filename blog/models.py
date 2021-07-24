from django.db import models
from users.models import User

STATUS = (
  (0, "Draft"),
  (1, "Publish")
)

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
  updated_on = models.DateField(auto_now=True)
  preview = models.TextField()
  content = models.TextField()
  created_on = models.DateField(auto_now_add=True)
  status = models.IntegerField(choices=STATUS, default=0)

  class Meta:
    ordering = ['-created_on']

  def __str__(self):
    return self.title

class Image(models.Model):
  name = models.CharField(max_length=200, unique=True)
  image = models.ImageField(upload_to='blog/')

  def __str__(self):
    return self.name