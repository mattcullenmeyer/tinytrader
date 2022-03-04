
## Introduction

I've been interested lately in different strategies for buying and selling crypocurrencies. Common advice for beginners is to buy only Bitcoin and Ethereum. The reasoning is that these two coins make up a large percentage of the total market and have remained dominant despite the rise and fall of other coins over time. Another strategy is to buy only the top 10 or so coins (excluding stable coins and - depending who you ask - meme coins). 

I was especially intrigued by Leigh Drogen's discussion of Starkiller Capital 

``` python
import pandas as pd

# load dataset
df = pd.read_csv('Historical Bitcoin Prices.csv')

# calculate daily returns
df['return'] = df['price'] / df['price'].shift(1) - 1

# add 5- and 50-day exponential moving averages
df['ema5'] = df.price.ewm(span=5, min_periods=5, adjust=False).mean()
df['ema50'] = df.price.ewm(span=50, min_periods=50, adjust=False).mean()
```

