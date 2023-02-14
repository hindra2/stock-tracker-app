# Library Import
import pickle

# InputStock class is used for storing and loading stocks that the user is tracking
class InputStock:
    def __init__(self, ticker, count, buy_price, lower_bound, upper_bound):
        self.ticker = ticker
        self.count = count
        self.buy_price = buy_price
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        self.database = open("user_stock", "ab")
    
    # Pickles bought stock info
    def dump_data(self):
        data = {
            self.ticker: {
                "Count": self.count,
                "Bought Price": self.buy_price,
                "Lower Bound": self.lower_bound,
                "Upper Bound": self.upper_bound,
            }
        }

        pickle.dump(data, self.database)
    
    # Loads picked data
    def load_data(self):
        data = pickle.load(self.database)