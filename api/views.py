from django.views.generic.base import TemplateView
from rest_framework import viewsets, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from api import serializers
# import time
import requests
import pandas as pd
import json
from datetime import datetime

# https://www.django-rest-framework.org/api-guide/viewsets/
# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

# https://www.django-rest-framework.org/topics/documenting-your-api/
class OpenApiView(TemplateView):
  template_name = 'api/documentation.html'
  extra_context = {'schema_url': 'api:schema_view'}

class TickerViewSet(viewsets.ModelViewSet):
  queryset = models.Ticker.objects.all()
  serializer_class = serializers.TickerSerializer
  lookup_field = 'ticker'
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SectorViewSet(viewsets.ModelViewSet):
  queryset = models.Sector.objects.all()
  serializer_class = serializers.SectorSerializer

class IndustryViewSet(viewsets.ModelViewSet):
  queryset = models.Industry.objects.all()
  serializer_class = serializers.IndustrySerializer

class SizeViewSet(viewsets.ModelViewSet):
  queryset = models.MarketCapSize.objects.all()
  serializer_class = serializers.SizeSerializer

class LiquidityViewSet(viewsets.ModelViewSet):
  queryset = models.Liquidity.objects.all()
  serializer_class = serializers.LiquiditySerializer

class MetadataViewSet(viewsets.ModelViewSet):
  queryset = models.Metadata.objects.all()
  serializer_class = serializers.MetadataSerializer
  lookup_field = 'ticker'
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  filterset_fields = '__all__' # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend

class MetricViewSet(viewsets.ModelViewSet):
  queryset = models.Metric.objects.all()
  serializer_class = serializers.MetricSerializer
  lookup_field = 'ticker'
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  #filterset_fields = '__all__'

class CryptoViewSet(viewsets.ModelViewSet):
  queryset = models.Crypto.objects.all()
  serializer_class = serializers.CryptoSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  lookup_field = 'slug'
  filter_backends = [filters.SearchFilter]
  search_fields = ['name']

class CryptoPricesHistoricalViewSet(viewsets.ModelViewSet):
  queryset = models.CryptoPrices.objects.all().order_by('-date')
  serializer_class = serializers.CryptoPricesSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  filterset_fields = ('crypto_id', )

class CryptoPricesLiveViewSet(APIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  def get(self, request, *args, **kwargs):
    coin_id = kwargs.get('id')
    # timeEnd = int(time.time())
    # timeStart = timeEnd - 86400 * 90
    # url = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?' \
    #   f'id={coin_id}&convertId=2781&timeStart={timeStart}&timeEnd={timeEnd}'

    url = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart?id={coin_id}&range=ALL'
    
    r = requests.get(url)
    data = r.json()

    # quotes = data['data']['quotes']
    quotes = data['data']['points']

    market_data = []
    for quote in quotes:
      date = datetime.fromtimestamp(int(quote))
      temp = quotes[quote]['v']
      # numbers = [n for n in temp[:3] if n != 0]
      # price = min(numbers)
      price, volume = temp[:2]
      market_data.append({
        'unix': quote,
        'date': date.strftime('%m/%d/%Y'),
        # 'date': date,
        'price': price,
        'volume': volume
      })
  
    # market_data = []
    # for quote in quotes:
    #   temp = quote['quote']
    #   date = pd.to_datetime(temp['timestamp'])
    #   # date = temp['timestamp']
    #   price = temp['close']
    #   volume = temp['volume']
    #   market_data.append({
    #     'date': date.strftime('%m/%d/%Y'),
    #     # 'date': date,
    #     'price': price,
    #     'volume': volume
    #   })

    columns=['unix', 'date', 'price', 'volume']
    # columns=['date', 'price']
    df = pd.DataFrame(market_data, columns=columns)
    df.sort_values(by='unix', inplace=True)

    df['ema5'] = df.price.ewm(span=5, min_periods=5, adjust=False).mean()
    df['ema50'] = df.price.ewm(span=50, min_periods=50, adjust=False).mean()

    result = df[-182:].to_json(orient='records')
    # result = df.to_json(orient='records')
    parsed = json.loads(result)

    return Response(parsed)