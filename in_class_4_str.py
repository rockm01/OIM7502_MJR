import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick # optional may be helpful for plotting percentage
import numpy as np
import numpy.matlib
import pandas as pd
import seaborn as sb # optional to set plot theme
import yfinance as yf
sb.set_theme() # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()


    def get_data(self):
        """method that downloads data and stores in a DataFrame
           uncomment the code below which should be the final two lines
           of your method"""
        tick = yf.Ticker(self.symbol)
        stock_data = tick.history(start=self.start, end=self.end)
        return stock_data

    
    def calc_returns(self, df):
        """method that adds change and return columns to data"""
        #change start and end date to match data that is pulled with yfinance
        start_dt = dt.date.isoformat(dt.date.today() - dt.timedelta(364))
        end_dt = dt.date.isoformat(dt.date.today() - dt.timedelta(3))
        start_price = self.data.loc[start_dt, 'Close']
        end_price = self.data.loc[end_dt, 'Close']
        delta = end_price - start_price
        return delta

    
    def plot_return_dist(self):
        """method that plots instantaneous returns as histogram"""
        self.data['rt'] = np.log(self.data['Close']) - np.log(self.data['Open']) #instantaneous return estimated using _
                                                                                 #daily open/close values
        plt.hist(self.data['rt'], bins=30, density=True, edgecolor='w')
        plt.show()


    def plot_performance(self):
        """method that plots stock object performance as percent """
        self.data['pct'] = self.data['Close'].pct_change()
        fig, ax = plt.subplots()
        ax.plot(self.data['pct'], linewidth=2.0)
        plt.show()


def main():
    pass

if __name__ == '__main__':
    mystock = Stock(symbol="AAPL")
    mystock.get_data()
    print("Calculated Return: ",mystock.calc_returns(df=mystock.data))
    print(mystock.plot_return_dist())
    print(mystock.plot_performance())
