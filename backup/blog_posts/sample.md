<div class="flex-center">
  <img alt="Historical stock volatility histogram for Apple Inc (AAPL)" src="/media/blog/aapl-historical-volatiliity-histogram.png" >
</div>

The following Python script is used to automatically export stock prices for a given company and compute its historical volatility over 12 months. The volatility calculations are especially helpful when compared to the implied volatility of a stock option, which can indicate whether that option is over- or under-valued. The script concludes with instructions on how to visualize the historical distribution of returns with a histogram plot.

##1. Import Python Libraries

You will first need to import the necessary Python libraries for this exercise. The <span class="highlight-text">yahoofinancials</span> library automatically exports historical stock prices without requiring you to do any of the web scraping yourself. The <span class="highlight-text">datetime</span> import is necessary for setting the start and end dates used in exporting stock prices over a specific time range. The <span class="highlight-text">pandas</span> and <span class="highlight-text">numpy</span> python libraries are indispensable whenever you're doing data analysis or scientific computing, respectively. Lastly, <span class="highlight-text">matplotlib</span> is a plotting library that makes it very easy to create data visualizations in Python, though not necessarily the most elegant option (for that I would recommend <span class="highlight-text">bokeh</span>).

``` python
from yahoofinancials import YahooFinancials
from datetime import date, timedelta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

##2. Export Historical Stock Prices

After importing Python libraries, the next step is to **export historical stock prices**. I will use Apple Inc (AAPL) as an illustrative example here, but you can easily change the <span class="highlight-text">stock_symbol</span> to the ticker of your choice. We're interested in **historical price volatility** over the last twelve months, therefore the <span class="highlight-text">start_time</span> is set to 365 days ago. The <span class="highlight-text">yahoofinancials</span> library requires dates to be in the format of 'year-month-day', hence the reformatting. Historical stock price data is pulled by 'daily', 'weekly' or 'monthly' time intervals through the <span class="highlight-text">yahoofinancials</span> module. 

``` python
# set stock ticker symbol
stock_symbol = 'AAPL'
 
# set date range for historical prices
end_time = date.today()
start_time = end_time - timedelta(days=365)
 
# reformat date range
end = end_time.strftime('%Y-%m-%d')
start = start_time.strftime('%Y-%m-%d')
 
# get daily stock prices over date range
json_prices = YahooFinancials(stock_symbol
    ).get_historical_price_data(start, end, 'daily')
```

##3. Convert JSON to Pandas DataFrame

Stock prices are returned through <span class="highlight-text">yahoofinanicals</span> in the JSON format, which is not particularly conducive to **data analysis**. For that we will use a <span class="highlight-text">pandas DataFrame</span> in Python. The JSON file contains a lot of data, but we're just interested in historical 'prices' for this exercise, specifically the daily price at market 'close' (and of course the trading date, indicated by the 'formatted_date' field). I then sort the prices in descending order to more easily calculate daily stock returns in the next step.

``` python
# transform json file to dataframe
prices = pd.DataFrame(json_prices[stock_symbol]
    ['prices'])[['formatted_date', 'close']]
 
# sort dates in descending order
prices.sort_index(ascending=False, inplace=True)
```

##4. Calculate Daily Stock Returns and Historical Price Volatility

Now that the historical stock prices are sorted in descending order, we can next calculate the **daily stock returns**. This is accomplished by taking the **natural log** of each day's closing stock price divided by the previous day's closing stock price. The <span class="highlight-text">numpy</span> library is then used to calculate the **standard deviation** of daily price returns. In order to calculate annualized volatility, we multiply the daily standard deviation by the square root of 252, which is the approximate number of trading days in a year.

``` python
# calculate daily logarithmic return
prices['returns'] = (np.log(prices.close /
    prices.close.shift(-1)))
      
# calculate daily standard deviation of returns
daily_std = np.std(prices.returns)
  
# annualized daily standard deviation
std = daily_std * 252 ** 0.5
```

##5. Plot Histogram of Daily Stock Returns

The only thing left to do at this point is to visualize the distribution of daily stock returns over the past year through a **histogram chart**. I use the <span class="highlight-text">matplotlib</span> library to do this, though it's pretty bare bones in all honesty. I recommend using a library like <span class="highlight-text">bokeh</span> if you want to create more stunning visualizations. 

``` python
# Plot histograms
fig, ax = plt.subplots(1, 1, figsize=(7, 5))
n, bins, patches = ax.hist(
    prices.returns.values,
    bins=50, alpha=0.65, color='blue')
 
ax.set_xlabel('log return of stock price')
ax.set_ylabel('frequency of log return')
ax.set_title('Historical Volatility for ' +
    stock_symbol)
  
# get x and y coordinate limits
x_corr = ax.get_xlim()
y_corr = ax.get_ylim()
  
# make room for text
header = y_corr[1] / 5
y_corr = (y_corr[0], y_corr[1] + header)
ax.set_ylim(y_corr[0], y_corr[1])
 
# print historical volatility on plot
x = x_corr[0] + (x_corr[1] - x_corr[0]) / 30
y = y_corr[1] - (y_corr[1] - y_corr[0]) / 15
ax.text(x, y , 'Annualized Volatility: ' + str(np.round(std*100, 1))+'%',
    fontsize=11, fontweight='bold')
x = x_corr[0] + (x_corr[1] - x_corr[0]) / 15
y -= (y_corr[1] - y_corr[0]) / 20
 
# save histogram plot of historical price volatility
fig.tight_layout()
fig.savefig('historical volatility.png')
```