from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from api import serializers
import time
import requests
import pandas as pd
import json

# https://www.django-rest-framework.org/api-guide/viewsets/
# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

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
  lookup_field = 'symbol'

class CryptoPricesHistoricalViewSet(viewsets.ModelViewSet):
  queryset = models.CryptoPrices.objects.all().order_by('-date')
  serializer_class = serializers.CryptoPricesSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  filterset_fields = ('crypto_id', )

class CryptoPricesLiveViewSet(APIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  
  def get(self, request, *args, **kwargs):
    coin_id = kwargs.get('id')
    timeEnd = int(time.time())
    timeStart = timeEnd - 86400 * 365 * 1
    url = f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id={coin_id}&convertId=2781&timeStart={timeStart}&timeEnd={timeEnd}'
    
    r = requests.get(url)
    data = r.json()

    quotes = data['data']['quotes']
  
    market_data = []
    for quote in quotes:
      temp = quote['quote']
      date = pd.to_datetime(temp['timestamp'])
      price = temp['close']
      volume = temp['volume']
      market_data.append({
        'date': date.strftime('%Y-%m-%d'),
        'price': price,
        'volume': volume
      })

    columns=['date', 'price', 'volume']
    df = pd.DataFrame(market_data, columns=columns)

    df['ema5'] = df.price.ewm(span=5, min_periods=5, adjust=False).mean()
    df['ema50'] = df.price.ewm(span=50, min_periods=50, adjust=False).mean()

    result = df.to_json(orient='records')
    parsed = json.loads(result)

    return Response(parsed)