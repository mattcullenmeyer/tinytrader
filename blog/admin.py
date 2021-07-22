from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
  readonly_fields = ('created_on', 'updated_on',)

admin.site.register(Post, PostAdmin)