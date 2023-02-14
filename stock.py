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

    def calc_total_cost(self, count, buy_price):
        return count*buy_price

    def calc_total_gain(self, count, buy_price):
        super().getCurrentPrice()
        curr_total = self.getCurrentPrice()*count
        total = self.calc_total_cost(count, buy_price)
        print(f"asdasd {(curr_total - total)/curr_total}")

        return round((curr_total - total)/curr_total, 2)
    
    # Function to update stock
    @classmethod
    def multithreading_stock():
        data_list = []

        with open("user_stock", "rb") as f:
            try:
                while True:
                    data = pickle.load(f)
                    data_list.append(data)
            except EOFError:
                print("Done loading data")
        f.close()

        for dict_ in data_list:
            cost = self.calc_total_cost(dict_["Count"], dict_["Bought Price"])
            gain = self.calc_total_gain(dict_["Count"], dict_["Bought Price"])
            dict_["Cost"] = cost
            dict_["Gain"] = gain
        
        with open("user_stock", "wb") as f:
            pickle.dump(data, f)
        f.close()

    
    def dump_data(self):
        try:
            cost = self.calc_total_cost(self.count, self.buy_price)
            gain = self.calc_total_gain(self.count, self.buy_price) 
            data = {
                self.ticker_str: {
                    "Count": self.count,
                    "Bought Price": self.buy_price,
                    "Cost": cost,
                    "Gain": gain
                }
            }

            database = open("user_stock", "wb")
            pickle.dump(data, database)
            database.close()
        except TypeError as e:
            print(e)
    
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

