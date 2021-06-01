from django.views.generic import TemplateView

class HomeView(TemplateView):
  template_name = 'pages/home.html'

class StockView(TemplateView):
  template_name = 'pages/stock.html'