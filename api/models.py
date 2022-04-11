from django.db import models

class Ticker(models.Model):
	ticker = models.CharField(max_length=6, unique=True)
	company_name_ticker = models.CharField(max_length=200, blank=True, null=True, default='')

	def __str__(self):
		return f'{self.id} {self.company_name_ticker}'

class Sector(models.Model):
	sector = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return f'{self.id} {self.sector}'

class Industry(models.Model):
	industry = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return f'{self.id} {self.industry}'

class MarketCapSize(models.Model):
	market_cap_size = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return f'{self.id} {self.market_cap_size}'

class Liquidity(models.Model):
  liquidity = models.CharField(max_length=100, unique=True)

  def __str__(self):
    return f'{self.id} {self.liquidity}'

class Metadata(models.Model):
  ticker = models.OneToOneField(Ticker, on_delete=models.CASCADE)

  sector = models.ForeignKey(Sector, on_delete=models.CASCADE, blank=True, null=True)
  industry = models.ForeignKey(Industry, on_delete=models.CASCADE, blank=True, null=True)
  market_cap_size = models.ForeignKey(MarketCapSize, on_delete=models.CASCADE, blank=True, null=True)
  liquidity = models.ForeignKey(Liquidity, on_delete=models.CASCADE, blank=True, null=True)

  price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  fiftyTwoWeekHigh = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  fiftyTwoWeekLow = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  bid = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  ask = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  volume = models.IntegerField(blank=True, null=True) # max of +/- 2 billion with IntegerField
  avg_volume = models.IntegerField(blank=True, null=True) 
  market_cap = models.BigIntegerField(blank=True, null=True)
  company_name = models.CharField(max_length=200, blank=True, null=True)
	
  last_updated = models.DateField(blank=True, null=True) # timestamp of when data was last refreshed

	# final ranks
  composite_rank = models.IntegerField(blank=True, null=True) 
  value_rank = models.IntegerField(blank=True, null=True) 
  mom_rank = models.IntegerField(blank=True, null=True) 
  quality_rank = models.IntegerField(blank=True, null=True) 
  vol_rank = models.IntegerField(blank=True, null=True) 
  profit_rank = models.IntegerField(blank=True, null=True) 
  finance_rank  = models.IntegerField(blank=True, null=True)  
  safety_rank = models.IntegerField(blank=True, null=True) 

  def __str__(self):
    return f'{self.ticker}'
	
class Metric(models.Model):
	ticker = models.OneToOneField(Ticker, on_delete=models.CASCADE)

	# averages
	composite_avg = models.FloatField(blank=True, null=True)
	value_avg = models.FloatField(blank=True, null=True)
	mom_avg = models.FloatField(blank=True, null=True)
	quality_avg = models.FloatField(blank=True, null=True)
	vol_avg = models.FloatField(blank=True, null=True)
	profit_avg = models.FloatField(blank=True, null=True)
	finance_avg = models.FloatField(blank=True, null=True)
	safety_avg = models.FloatField(blank=True, null=True)

	# value 
	pe_value = models.FloatField(blank=True, null=True)
	pe_sec_median = models.FloatField(blank=True, null=True)
	pe_sec_rank = models.IntegerField(blank=True, null=True)
	pe_ind_median = models.FloatField(blank=True, null=True)
	pe_ind_rank = models.IntegerField(blank=True, null=True)
	pb_value = models.FloatField(blank=True, null=True)
	pb_sec_median = models.FloatField(blank=True, null=True)
	pb_sec_rank = models.IntegerField(blank=True, null=True)
	pb_ind_median = models.FloatField(blank=True, null=True)
	pb_ind_rank = models.IntegerField(blank=True, null=True)
	ps_value = models.FloatField(blank=True, null=True)
	ps_sec_median = models.FloatField(blank=True, null=True)
	ps_sec_rank = models.IntegerField(blank=True, null=True)
	ps_ind_median = models.FloatField(blank=True, null=True)
	ps_ind_rank = models.IntegerField(blank=True, null=True)
	pcf_value = models.FloatField(blank=True, null=True)
	pcf_sec_median = models.FloatField(blank=True, null=True)
	pcf_sec_rank = models.IntegerField(blank=True, null=True)
	pcf_ind_median = models.FloatField(blank=True, null=True)
	pcf_ind_rank = models.IntegerField(blank=True, null=True)
	eve_value = models.FloatField(blank=True, null=True)
	eve_sec_median = models.FloatField(blank=True, null=True)
	eve_sec_rank = models.IntegerField(blank=True, null=True)
	eve_ind_median = models.FloatField(blank=True, null=True)
	eve_ind_rank = models.IntegerField(blank=True, null=True)

	# momentum
	mom_12_value = models.FloatField(blank=True, null=True)
	mom_12_sec_median = models.FloatField(blank=True, null=True)
	mom_12_sec_rank = models.IntegerField(blank=True, null=True)
	mom_12_ind_median = models.FloatField(blank=True, null=True)
	mom_12_ind_rank = models.IntegerField(blank=True, null=True)
	mom_6_value = models.FloatField(blank=True, null=True)
	mom_6_sec_median = models.FloatField(blank=True, null=True)
	mom_6_sec_rank = models.IntegerField(blank=True, null=True)
	mom_6_ind_median = models.FloatField(blank=True, null=True)
	mom_6_ind_rank = models.IntegerField(blank=True, null=True)

	# volatility
	vol_12_value = models.FloatField(blank=True, null=True)
	vol_12_sec_median = models.FloatField(blank=True, null=True)
	vol_12_sec_rank = models.IntegerField(blank=True, null=True)
	vol_12_ind_median = models.FloatField(blank=True, null=True)
	vol_12_ind_rank = models.IntegerField(blank=True, null=True)
	beta_value = models.FloatField(blank=True, null=True)
	beta_sec_median = models.FloatField(blank=True, null=True)
	beta_sec_rank = models.IntegerField(blank=True, null=True)
	beta_ind_median = models.FloatField(blank=True, null=True)
	beta_ind_rank = models.IntegerField(blank=True, null=True)

	# profit
	asset_turn_value = models.FloatField(blank=True, null=True)
	asset_turn_sec_median = models.FloatField(blank=True, null=True)
	asset_turn_sec_rank = models.IntegerField(blank=True, null=True)
	asset_turn_ind_median = models.FloatField(blank=True, null=True)
	asset_turn_ind_rank = models.IntegerField(blank=True, null=True)
	gross_profit_value = models.FloatField(blank=True, null=True)
	gross_profit_sec_median = models.FloatField(blank=True, null=True)
	gross_profit_sec_rank = models.IntegerField(blank=True, null=True)
	gross_profit_ind_median = models.FloatField(blank=True, null=True)
	gross_profit_ind_rank = models.IntegerField(blank=True, null=True)
	gross_margin_value = models.FloatField(blank=True, null=True)
	gross_margin_sec_median = models.FloatField(blank=True, null=True)
	gross_margin_sec_rank = models.IntegerField(blank=True, null=True)
	gross_margin_ind_median = models.FloatField(blank=True, null=True)
	gross_margin_ind_rank = models.IntegerField(blank=True, null=True)
	return_asset_value = models.FloatField(blank=True, null=True)
	return_asset_sec_median = models.FloatField(blank=True, null=True)
	return_asset_sec_rank = models.IntegerField(blank=True, null=True)
	return_asset_ind_median = models.FloatField(blank=True, null=True)
	return_asset_ind_rank = models.IntegerField(blank=True, null=True)

	# finance
	ext_fin_value = models.FloatField(blank=True, null=True)
	ext_fin_sec_median = models.FloatField(blank=True, null=True)
	ext_fin_sec_rank = models.IntegerField(blank=True, null=True)
	ext_fin_ind_median = models.FloatField(blank=True, null=True)
	ext_fin_ind_rank = models.IntegerField(blank=True, null=True)
	cf_debt_value = models.FloatField(blank=True, null=True)
	cf_debt_sec_median = models.FloatField(blank=True, null=True)
	cf_debt_sec_rank = models.IntegerField(blank=True, null=True)
	cf_debt_ind_median = models.FloatField(blank=True, null=True)
	cf_debt_ind_rank = models.IntegerField(blank=True, null=True)

	# safety
	accrual_value = models.FloatField(blank=True, null=True)
	accrual_sec_median = models.FloatField(blank=True, null=True)
	accrual_sec_rank = models.IntegerField(blank=True, null=True)
	accrual_ind_median = models.FloatField(blank=True, null=True)
	accrual_ind_rank = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return f'{self.ticker}'

class Crypto(models.Model):
  id = models.IntegerField(primary_key=True)
  symbol = models.CharField(max_length=6, unique=True, blank=True, null=True)
  name = models.CharField(max_length=200, blank=True, null=True)
  slug = models.SlugField(max_length=200, blank=True, null=True)

  def __str__(self):
    return f'{self.symbol}'

class CryptoPrices(models.Model):
  crypto_id = models.ForeignKey(Crypto, on_delete=models.CASCADE, blank=True, null=True)
  date = models.DateField(blank=True, null=True)
  price = models.FloatField(blank=True, null=True)
  volume = models.FloatField(blank=True, null=True)
  market_cap = models.FloatField(blank=True, null=True)
