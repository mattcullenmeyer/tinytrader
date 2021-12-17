from rest_framework import serializers
from users import models

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.User
    fields = ('id', 'email', 'email_verified', 'username', 'first_name', 'last_name')