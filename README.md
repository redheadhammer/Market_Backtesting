# Strategy backtesting

This project focuses on backtesting stocks data in a specific time frame.

# Steps

1. Fetch Historic data from various data providers. In this we will be using yahoo finance

## Fetch data using yfinance

1. install [yfinance](https://github.com/ranaroussi/yfinance) using `pip install yfinance`

2. fetch data using yfinance with below code snippet
   ```python
   import yfinance as yf
   data = yf.download(
               "VOLTAS.NS",
               start="2022-02-22 10:30:30",
               end="2022-02-22 11:30:30",
               interval="10m"
           )
   # period = "1d" can be used too
   ```
3. download will return **Pandas Dataframe** with historic data

4. Extract a specific column or row from data using `data["column name"]` i.e. `data["open"]`.

5. In general Dataframe is just a table with some rows and columns. We can filter content using `loc` method of DataFrame. `data.loc[['row1', ['row2']], ['col3', 'col5']]`

   ```python
   # data.index(['index1', 'index2', 'index3'])
   data.loc[['row1', 'row3'], ['col1', 'col4', 'col7']] # this will print row1, row3 and given cols only.
   ```

6. Below code contains many basic things about yfinance api

   ```python
   import yfinance as yf

   msft = yf.Ticker("MSFT")

   # get all stock info
   msft.info

   # get historical market data
   hist = msft.history(period="1mo")

   # show meta information about the history (requires history() to be called first)
   msft.history_metadata

   # show actions (dividends, splits, capital gains)
   msft.actions
   msft.dividends
   msft.splits
   msft.capital_gains  # only for mutual funds & etfs

   # show share count
   # - yearly summary:
   msft.shares
   # - accurate time-series count:
   msft.get_shares_full(start="2022-01-01", end=None)

   # show financials:
   # - income statement
   msft.income_stmt
   msft.quarterly_income_stmt
   # - balance sheet
   msft.balance_sheet
   msft.quarterly_balance_sheet
   # - cash flow statement
   msft.cashflow
   msft.quarterly_cashflow
   # see `Ticker.get_income_stmt()` for more options

   # show holders
   msft.major_holders
   msft.institutional_holders
   msft.mutualfund_holders

   # show earnings
   msft.earnings
   msft.quarterly_earnings

   # show sustainability
   msft.sustainability

   # show analysts recommendations
   msft.recommendations
   msft.recommendations_summary
   # show analysts other work
   msft.analyst_price_target
   msft.revenue_forecasts
   msft.earnings_forecasts
   msft.earnings_trend

   # show next event (earnings, etc)
   msft.calendar

   # Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
   # Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
   msft.earnings_dates

   # show ISIN code - *experimental*
   # ISIN = International Securities Identification Number
   msft.isin

   # show options expirations
   msft.options

   # show news
   msft.news

   # get option chain for specific expiration
   opt = msft.option_chain('YYYY-MM-DD')
   # data available via: opt.calls, opt.puts
   ```

## Plot DataValues

A `DataFrame` can have many rows or columns but to draw a 2d graph we need 2 values. To draw using **matplotlib** we need to provide values for 2 axis.

`plt.plot(xaxis-data, yaxis-data, color="blue", label="time")`

```python
data["change"] = [val+816 for val in data["Close"].pct_change()]

timestamps = data.index
times = [val.strftime('%H:%M') for val in timestamps]

plt.plot(times, data["Close"], color="blue", label="price line")
plt.plot(times, data["change"], color="red", label="change line")
plt.title("Some title")
plt.xlabel("Time")
plt.ylabel("Price")
plt.xticks(rotation=90)
# set maximum number of values that can be placed on x-axis.
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(min(15, len(times))))
plt.show();
```

In some cases data on axis will be too much than available space than we can restrict it to some particular tick locations using `plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))` (this will set 10 ticks on xaxis).

We can plot other types of graphs too like pie-charts

```python
# importing pandas library
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
	'Object': ['Bulb', 'Lamp', 'Table', 'Pen', 'Notebook'],
	'Price': [45, 38, 90, 60, 40]
})

# plotting a pie chart
plt.pie(df["Price"], labels=df["Object"])
plt.show()
```

Create a scatter graphs with dots across graph.

```python
# importing pandas library
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
	'X': [1, 2, 3, 4, 5],
	'Y': [2, 4, 6, 10, 15]
})

# plotting a line graph
print("Line graph: ")
plt.plot(df["X"], df["Y"])
plt.show()

# plotting a scatter plot
print("Scatter Plot: ")
plt.scatter(df["X"], df["Y"])
plt.show()
```

Create a categories type graph

```python
# importing pandas library
import pandas as pd
# importing matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
	'Name': ['John', 'Sammy', 'Joe'],
	'Age': [45, 38, 90]
})

# plotting a bar graph
df.plot(x="Name", y="Age", kind="bar")
```
