class UserStock:
    def __init__(self, name, ticker, curr_price, buy_price):
        self.name = name
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