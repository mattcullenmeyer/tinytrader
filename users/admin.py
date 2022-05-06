from django.contrib import admin
from rest_framework_simplejwt import token_blacklist
from users import models

class UserAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)
  list_filter = ('email_verified',)

admin.site.register(models.User, UserAdmin)

# https://github.com/jazzband/djangorestframework-simplejwt/issues/266
# require ability to delete users, which is blocked by default using token_blacklist
class OutstandingTokenAdmin(token_blacklist.admin.OutstandingTokenAdmin):

    def has_delete_permission(self, *args, **kwargs):
        return True

admin.site.unregister(token_blacklist.models.OutstandingToken)
admin.site.register(token_blacklist.models.OutstandingToken, OutstandingTokenAdmin)
