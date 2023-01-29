import yfinance as yf
import matplotlib.pyplot as plt
from mplcursors import cursor
import pandas
import tkinter as tk


class Stock:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)
        self.name = self.ticker.info["longName"]
        self.openingPrice = self.ticker.fast_info["open"]
        self.highPrice = self.ticker.fast_info["day_high"]
        self.lowPrice = self.ticker.fast_info["day_low"]
        self.volume = self.ticker.fast_info['last_volume']
        self.history = self.ticker.history(period='1y')
        self.currentPrice = self.ticker.fast_info["last_price"]

    def getOpeningPrice(self, tickers):
        return round(self.openingPrice)

    def getPriceRange(self):
        return self.highPrice - self.lowPrice

    def getVolume(self):
        return self.volume

    def getHistory(self):
        return self.history

    def getName(self):
        return self.name

    def plotHistory(self, type):
        graph = plt.figure()
        plt.plot(self.history.index,self.history[type], marker=".", label=type)
        plt.ylabel("Price (USD)")
        plt.xlabel("Date (Year)")
        cursor(hover=True)
        plt.legend()
        return graph


class TopStocks(Stock):
    def __init__(self, index, history, ticker):
        super().__init__(ticker)
        self.index = index
        self.history = history

    def scrapeGain(index):
        pass