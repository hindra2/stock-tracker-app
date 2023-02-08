import yfinance as yf
import matplotlib.pyplot as plt
from mplcursors import cursor
import pandas
import tkinter as tk
import pickle
import os

database_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "user_stock")

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
        graph = plt.figure()
        self.getHistory(period)
        plt.plot(self.history.index,self.history[type1], marker=".", label=type1)
        plt.plot(self.history.index,self.history[type2], marker=".", label=type2)
        plt.ylabel("Price (USD)")
        plt.xlabel("Date (Year)")
        cursor(hover=True)
        plt.legend()
        return graph

class InputStock(Stock):
    def __init__(self, ticker, count, buy_price, lower_bound, upper_bound):
        super().__init__(ticker)
        self.ticker = ticker
        self.count = count
        self.buy_price = buy_price
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
    
    def dump_data(self):
        try:
            data = {
                self.ticker: {
                    "Count": self.count,
                    "Bought Price": self.buy_price,
                    "Upper Bound": self.upper_bound,
                    "Lower Bound": self.lower_bound
                }
            }

            database = open("user_stock", "ab")
            pickle.dump(data, database)
            database.close()
        except TypeError:
            print("No Ticker Specified")
    
    @classmethod
    def load_data(cls):
        try:
            data_list = []

            with open("user_stock", "rb") as f:
                    try:
                        while True:
                            data = pickle.load(f)
                            data_list.append(data)
                    except EOFError:
                        print("Done loading data")
            
            return data_list

        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error loading data: {e}")
                
        except EOFError:
            print("No data in database or corrupted data")
        
        finally:
            f.close()

