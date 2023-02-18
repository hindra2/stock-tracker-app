import yfinance as yf
import matplotlib.pyplot as plt
from mplcursors import cursor
import pandas
import tkinter as tk
import pickle
import os

class Stock:
    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)
        self.ticker_str = ticker
    
    def getCurrentPrice(self):
        self.currentPrice = self.ticker.fast_info["last_price"]
        return self.currentPrice

    def getOpeningPrice(self):
        self.openingPrice = self.ticker.fast_info["open"]
        return round(self.openingPrice)

    def getPriceRange(self):
        self.highPrice = self.ticker.fast_info["day_high"]
        self.lowPrice = self.ticker.fast_info["day_low"]
        return self.highPrice - self.lowPrice

    def getVolume(self):
        self.volume = self.ticker.fast_info['last_volume']
        return self.volume

    def getHistory(self, period):
        self.history = self.ticker.history(period=period)
        return self.history

    def getName(self):
        return self.ticker_str

    def plotHistory(self, type1, type2, period):
        try:
            graph = plt.figure()
            self.getHistory(period)
            plt.plot(self.history.index,self.history[type1], marker=".", label=type1)
            plt.plot(self.history.index,self.history[type2], marker=".", label=type2)
            plt.ylabel("Price (USD)")
            plt.xlabel("Date (Year)")
            cursor(hover=True)
            plt.legend()
            return graph
        except AttributeError as e:
            print(f"Error: {e}")
            print("User probably didn't enter a ticker in the entry field")

class InputStock(Stock):
    def __init__(self, ticker_str, count, buy_price):
        super().__init__(ticker_str)
        self.count = int(count)
        self.buy_price = int(buy_price)
    
    def dump_data(self):
        try:
            cost =self.count*self.buy_price
            gain = self.calc_total_gain(self.count, self.buy_price) 
            data = {
                self.ticker_str: {
                    "Count": self.count,
                    "Bought Price": self.buy_price,
                    "Cost": cost,
                    "Gain": gain
                }
            }

            with open("user_stock", "ab") as f:
                pickle.dump(data, f)
            f.close()
        except TypeError as e:
            print(e)

    def calc_total_gain(self, count, buy_price):
        super().getCurrentPrice()
        curr_total = self.getCurrentPrice()*count
        total = count*buy_price
        print(f"asdasd {(curr_total - total)/curr_total}")

        return round((curr_total - total)/curr_total, 2)

    @classmethod
    def load_data(cls):
        try:
            data_list = []

            with open("user_stock", "rb") as f:
                while True:
                    try:
                        data = pickle.load(f)
                    except EOFError:
                        break
                    data_list.append(data)
            
            pass
            return data_list

        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error loading data: {e}")
        
        finally:
            f.close()

