import json

class InputStock:
    def __init__(self, ticker, count, buy_price, lower_bound, upper_bound):
        self.ticker = ticker
        self.count = count
        self.buy_price = buy_price
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
    
    def dump_data(self):
        data = {
            self.ticker: {
                "Count": self.count,
                "Bought Price": self.buy_price,
                "Upper Bound": self.upper_bound,
                "Lower Bound": self.lower_bound
            }
        }

        print(data)

        with open("stock_list.json", "w") as write_file:
            json.dump(data, write_file)

class DisplayStock:
    def __init__(self, ticker, curr_price, buy_price):
        self.ticker = ticker
        self.curr_price = curr_price
        self.buy_price = buy_price
        self.gain = ((curr_price - buy_price)/buy_price) * 100

    def get_name(self):
        return self.name

    def get_ticker(self):
        return self.ticker

    def get_curr_price(self):
        return self.curr_price

    def get_buy_price(self):
        return self.buy_price

    def get_gain(self):
        return self.gain

if __name__ == "__main__":
    InputStock("TSLA", 100, 15, 10, 23)