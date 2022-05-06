from rest_framework import serializers
from api import models

# https://www.django-rest-framework.org/api-guide/serializers

class TickerSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Ticker
    fields = '__all__' # you can't use __all__ with HyperlinkedModelSerializer
    #fields = ('id', 'ticker',)
    # https://stackoverflow.com/questions/32201257/django-rest-framework-access-item-detail-by-slug-instead-of-id
    lookup_field = 'ticker'
    extra_kwargs = {
      'url': {'lookup_field': 'ticker'}
    }

class SectorSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Sector
    fields = '__all__'

class IndustrySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Industry
    fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.MarketCapSize
    fields = '__all__'

class LiquiditySerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Liquidity
    fields = '__all__'

class MetadataSerializer(serializers.ModelSerializer):
  sector = SectorSerializer(read_only=True)
  industry = IndustrySerializer(read_only=True)
  market_cap_size = SizeSerializer(read_only=True)
  
  class Meta:
    model = models.Metadata
    fields = '__all__'
    lookup_field = 'ticker'
    extra_kwargs = {
      'url': {'lookup_field': 'ticker'}
    }

class MetricSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Metric
    fields = '__all__'
    lookup_field = 'ticker'
    extra_kwargs = {
      'url': {'lookup_field': 'ticker'}
    }

# https://www.django-rest-framework.org/api-guide/relations/#nested-relationships

class CryptoSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Crypto
    fields = '__all__'

class CryptoPricesSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.CryptoPrices
    fields = '__all__'

class EmailConfirmationSerializer(serializers.Serializer):
  email_address = serializers.CharField()
