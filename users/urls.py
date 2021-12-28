from django.urls import path
from users import views
from django.contrib.auth.decorators import login_required

app_name = 'users'
urlpatterns = [
  path('resend-verfication/', login_required(views.resend_verfication), name="resend_verfication"),
]
