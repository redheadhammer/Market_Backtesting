"""
This uses yfinance (yahoo finance) to get the historic data of a stock
INTRADAY DATA WILL BE ONLY AVAILABLE UPTO 60 DAYS, which seems sufficient
to me.
"""

import yfinance as yf
import pandas as pd
from pandas import DataFrame


def getRangeData(symbol, start = "2023-04-13", end = "2023-04-14", interval = "5m", rounding=True):
        try:
            return yf.download(
                symbol,
                start = start,
                end = end,
                interval = interval
            )
        except Exception:
            return None
    

def getPeriodData(symbol, period="1d", interval="5m"):
    """
    Don't use period with start and stop. Setting rounding to true
    will round the values to 2 decimal places.
    """
    try:
        return yf.download(
            symbol, 
            period=period, 
            interval=interval, 
            rounding=True
        )
    except Exception:
        return None




class history:
    def __init__(self, symbol) -> None:
        self.symbol = symbol

    def _getTicker(self):
        self.ticker = yf.Ticker(self.symbol)
    
    def getInfo(self):
        if (not self.ticker):
            self._getTicker()

        fields = [
                'sector', 
                'industry', 
                'fullTimeEmployees', 
                'city', 
                'state', 
                'country', 
                'exchange', 
                'shortName', 
                'longName', 
                # 'longBusinessSummary'
            ]

        corp_info = {k: v for k, v in self.ticker.info.items() if k in fields}
        df_info = pd.DataFrame.from_dict(corp_info, orient='index', columns=['AAPL'])

        # return self.ticker.info
        return df_info
    
    def getEarnings(self) -> dict[str, DataFrame]:
        if (not self.ticker):
            self._getTicker()

        return {"yearly": self.ticker.quarterly_earnings, "quarterly": self.ticker.earnings}
    
    def getNews(self):
        if (not self.ticker):
            self._getTicker()

        return self.ticker.news
    
    def getBalanceSheet(self):
        if (not self.ticker):
            self._getTicker()
            
        return {"yearly": self.ticker.balance_sheet, "quarterly": self.ticker.quarterly_balance_sheet}
    
    def getHolders(self):
        if (not self.ticker):
            self._getTicker()
            
        return {"instituional": self.ticker.institutional_holders, "major": self.ticker.major_holders}
    
    def getActions(self):
        if (not self.ticker):
            self._getTicker()
            
        return {
            "dividends": self.ticker.dividends,
            "splits": self.ticker.splits,
            "capital_gains": self.ticker.capital_gains
        }
    
    def earningDates(self):
        if (not self.ticker):
            self._getTicker()
            
        return self.ticker.earnings_dates
    
