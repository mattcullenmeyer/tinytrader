from django.contrib import admin
from api import models

admin.site.register(models.Ticker)
admin.site.register(models.Sector)
admin.site.register(models.Industry)
admin.site.register(models.MarketCapSize)
admin.site.register(models.Liquidity)
admin.site.register(models.Metadata)
admin.site.register(models.Metric)
admin.site.register(models.Crypto)