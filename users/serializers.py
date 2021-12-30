from rest_framework import serializers
from users import models
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.User
    fields = ('id', 'email', 'email_verified', 'username', 'first_name', 'last_name')

class SignupEmailSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.User
    fields = ('email',)

# https://github.com/jazzband/djangorestframework-simplejwt/blob/master/rest_framework_simplejwt/serializers.py
class CustomTokenRefreshSerializer(TokenRefreshSerializer):
  refresh = serializers.CharField()
  access = serializers.CharField(read_only=True)

  def validate(self, attrs):
    refresh = RefreshToken(attrs["refresh"])

    data = {"access_token": str(refresh.access_token)}

    if api_settings.ROTATE_REFRESH_TOKENS:
      if api_settings.BLACKLIST_AFTER_ROTATION:
        try:
          refresh.blacklist()
        except AttributeError:
          pass

      refresh.set_jti()
      refresh.set_exp()
      refresh.set_iat()

      data["refresh_token"] = str(refresh)

    return data