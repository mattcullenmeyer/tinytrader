from django.contrib import admin
from users import models

class UserAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)
  list_filter = ('email_verified',)

admin.site.register(models.User, UserAdmin)
