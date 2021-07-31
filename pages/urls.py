from django.urls import path
from pages import views

app_name = 'pages'
urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('about/', views.AboutView.as_view(), name='about'),
  path('privacy/', views.PrivacyView.as_view(), name='privacy'),
  path('terms/', views.TermsView.as_view(), name='terms'),

  path('stock/<ticker>/', views.StockView.as_view(), name='stock'),
]
