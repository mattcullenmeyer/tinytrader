from django.contrib import admin
from blog.models import Post, Image

class PostAdmin(admin.ModelAdmin):
  readonly_fields = ('created_on', 'id',)

admin.site.register(Post, PostAdmin)
admin.site.register(Image)