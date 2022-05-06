from django.urls import path
from users import views
from django.contrib.auth.decorators import login_required

app_name = 'users'
urlpatterns = [
  # TODO: Remove this url once fully transitioned frontend off Django and to React
  path('resend-verfication/', login_required(views.resend_verfication), name="resend_verfication"),
]
