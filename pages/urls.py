from django.urls import path
from pages.views import HomeView, StockView

app_name = 'pages'
urlpatterns = [
  path('', HomeView.as_view(), name='home'),

  path('stock/<ticker>/', StockView.as_view(), name='stock'),
]
