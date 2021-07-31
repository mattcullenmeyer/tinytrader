from django.urls import path
from pages.views import HomeView, AboutView, StockView, PrivacyView

app_name = 'pages'
urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('about/', AboutView.as_view(), name='about'),
  path('privacy/', PrivacyView.as_view(), name='privacy'),

  path('stock/<ticker>/', StockView.as_view(), name='stock'),
]
