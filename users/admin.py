from django.contrib import admin
from users import models

class UserAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)

admin.site.register(models.User, UserAdmin)
