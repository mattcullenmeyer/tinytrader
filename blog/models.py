from django.db import models
from users.models import User

STATUS = (
  (0, "Draft"),
  (1, "Publish"),
)

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True)
  slug = models.SlugField(max_length=200, unique=True)
  metadescription = models.CharField(max_length=200)
  author = models.ForeignKey(User, on_delete= models.PROTECT, related_name='blog_posts')
  updated_on = models.DateField()
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
  post = models.ForeignKey(Post, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} >> {self.post.slug}'

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  name = models.ForeignKey(User, on_delete= models.PROTECT, related_name='commenters')
  parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')
  body = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  active = models.BooleanField(default=True)

  class Meta:
    ordering = ['created_on']

  def __str__(self):
    return f'{self.name} >> {self.body}'
