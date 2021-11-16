from django.urls import path, include
from users import views
from django.contrib.auth.decorators import login_required

app_name = 'users'
urlpatterns = [
  path('resend-verfication/', login_required(views.resend_verfication), name="resend_verfication"),
  path('dj-rest-auth/', include('dj_rest_auth.urls')),
  path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
