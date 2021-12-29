from rest_framework.response import Response
from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from allauth.account.models import EmailAddress
from allauth.account.adapter import get_adapter
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework import viewsets, generics
from users import serializers
# from django.contrib.auth.models import User
from users import models
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenViewBase


# https://stackoverflow.com/questions/54467321/how-to-tell-if-users-email-address-has-been-verified-using-django-allauth-res
# make email_verified = True in users model whenever allauth email confirmation is made
@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = email_address.user
    user.email_verified = True

    user.save()

# https://stackoverflow.com/questions/66629248/allauth-resending-verification-redirects-to-another-page
# override allauth resend verification post request to redirect to desired page (ie stay on current/previous page)
def resend_verfication(request):
  if request.method == "POST":
    email = request.POST["email"]
    next = request.POST["next"]
    try:
      email_address = EmailAddress.objects.get(
        user=request.user,
        email=email,
      )
      get_adapter(request).add_message(
        request,
        messages.INFO,
        "account/messages/" "email_confirmation_sent.txt",
        {"email": email},
      )
      email_address.send_confirmation(request)
    except EmailAddress.DoesNotExist:
        pass
    return redirect(next)

class UsersViewSet(viewsets.ModelViewSet):
  queryset = models.User.objects.all()
  serializer_class = serializers.UserSerializer
  permission_classes = [permissions.IsAdminUser]

class UserDetailView(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
    serializer = serializers.UserSerializer(request.user)
    return Response(serializer.data)

class SignupEmailView(generics.RetrieveAPIView):
  serializer_class = serializers.SignupEmailSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = models.User.objects.all()
  lookup_field = 'email'

class CustomTokenRefreshView(TokenViewBase):
  serializer_class = serializers.CustomTokenRefreshSerializer