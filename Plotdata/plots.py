
import mplfinance as mpl



def basic_plot(data):
    mpl.plot(data, type='candle', mav=(3,6,9), volume=True, show_nontrading=True)


# how to use mpl to plot price movement and other indicators on it.
# plot 200ema and 50ema on graph of a stock

# write a function to add 3 numbers
