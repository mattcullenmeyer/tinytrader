from rest_framework.response import Response
from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from allauth.account.models import EmailAddress
from allauth.account.adapter import get_adapter
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework import viewsets, generics
from api.serializers import EmailConfirmationSerializer
from users import serializers
from users import models
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenViewBase
from allauth.account.models import EmailConfirmation
from rest_framework.decorators import api_view, permission_classes


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

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def email_confirmation(request, key):
  if request.method == 'GET':
    # key = request.data['key'] # use for post request if in request body
    email_confirmation = EmailConfirmation.objects.get(key=key)
    key_expired = email_confirmation.key_expired()
    serializer = EmailConfirmationSerializer(email_confirmation)
    return Response({
      "email_address": serializer.data['email_address'],
      "key_expired": key_expired
    })

class UsersViewSet(viewsets.ModelViewSet):
  queryset = models.User.objects.all()
  serializer_class = serializers.UserSerializer
  permission_classes = [permissions.IsAdminUser]

class UserDetailView(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticated]
  queryset = models.User.objects.all()
  def get(self, request):
    serializer = serializers.UserSerializer(request.user)
    return Response(serializer.data)

class SignupEmailView(generics.RetrieveAPIView):
  serializer_class = serializers.SignupEmailSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = models.User.objects.all()
  lookup_field = 'email'

class SignupUsernameView(generics.RetrieveAPIView):
  serializer_class = serializers.SignupUsernameSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = models.User.objects.all()
  lookup_field = 'username'

class CustomTokenRefreshView(TokenViewBase):
  serializer_class = serializers.CustomTokenRefreshSerializer