from django.contrib import admin
from blog.models import Post, Image, Comment

class PostAdmin(admin.ModelAdmin):
  readonly_fields = ('created_on', 'id',)
  list_filter = ('status',)

admin.site.register(Post, PostAdmin)
admin.site.register(Image)
admin.site.register(Comment)
