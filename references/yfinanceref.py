import yfinance as yf

tickers = yf.Ticker("MSFT")
# print(tickers.history("High"))
print(tickers.info["longName"])