"""
It is also possible to scrape Yahoo Finance Live stock quotes using
web scraping tools. The package yahoo_fin has done exactly that so
you can just call its functions if you don't want to write one yourself.
The following code gets the real-time stock price every second and then
save it for later use. It is suggested to run the code during market
hours. Usually, people start listening to the real-time stock price at
market open and then save the data at market close.
"""

import numpy as np
import pandas as pd
from yahoo_fin import stock_info
from datetime import datetime
import time

real_time_quotes = pd.DataFrame(columns=['time', 'price'])
# realtime quotes
for i in range(10):
    now = datetime.now()
    price = stock_info.get_live_price("SPY")
    print(now, 'SPY:', price)
    real_time_quotes.loc[i] = [now, price]
    time.sleep(1)
print(real_time_quotes)
# save for later use
# real_time_quotes.to_csv('realtime_tick_data.csv', index=False)