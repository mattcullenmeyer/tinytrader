from django.urls import path, include
from users import views
from django.contrib.auth.decorators import login_required
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView

app_name = 'users'
urlpatterns = [
  path('resend-verfication/', login_required(views.resend_verfication), name="resend_verfication"),
  path('dj-rest-auth/', include('dj_rest_auth.urls')),
  path('dj-rest-auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()), # Needs to be defined before registration path
  path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
  path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
  path('user/', views.UserView.as_view()),
]
