from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
import sys
import argparse

# Dow Jones
param = {
    'q': "AAPL", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "1Y" # Period (Ex: "1Y" = 1 year)
}

for arg in sys.argv:
    print(arg)


# get price data (return pandas dataframe)
df = get_price_data(param)
print(df)