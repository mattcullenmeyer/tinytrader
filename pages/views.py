from django.views.generic import TemplateView

class HomeView(TemplateView):
  template_name = 'pages/home.html'

class AboutView(TemplateView):
  template_name = 'pages/about.html'

class PrivacyView(TemplateView):
  template_name = 'pages/privacy.html'

class StockView(TemplateView):
  template_name = 'pages/stock.html'