
import yfinance as yf
import pandas as pd

URL = 'https://www1.nseindia.com/content/indices/ind_nifty50list.csv'
df = pd.read_csv(URL, index_col = 'Company Name')

print(df)
