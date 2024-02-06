"""
EMA or exponential moving average is used to find the trend signal of a stock.
It gives more importance to the recent prices than previous prices unlike 
Arithmetic Moving Average. It uses smoothing factor to give defined importance
to the recent prices.
"""

from pandas import DataFrame

class EMA:
    """
    Smoothing factor is a parameter that determines the weight given to recent data points.
    It is used to control the rate at which the EMA responds to changes in the price series.
    In general It is calculated as: SF = 2/(N+1). Where N will be the data points or size of
    data we are calculating EMA of.
    """
    def __calculateSF(self, size):
        return (2 / (size + 1))

    def getEMA(self, data: DataFrame):
        # closeData = self.data.loc[:, ["Close"]]
        # closeData = self.data["Close"]
        
        EMA = data["Close"][0]
        SF = self.__calculateSF(len(data))
        print(f"SF value is: {SF}")

        for value in data["Close"][1:]:
            EMA = (value * SF) + (EMA * (1 - SF))

        return EMA

