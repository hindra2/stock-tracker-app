import mainPage
import threading
import queue
import pickle
import time
import scraper
import stock

# This is the file the user runs

# Data Queues
news_queue = queue.Queue()
asset_queue = queue.Queue()

stock_updated = threading.Event()



def main(sq, aq, stock_updated):
    app = mainPage.MainApp(sq, aq, stock_updated)
    app.withdraw()

    def update_gui():
            app.update()
            app.after(1000, update_gui)

    update_gui()
    app.mainloop()

def thread1(sq):
    while True:
        bbc_list = scraper.scrape_bbc()
        yfinance_list = scraper.scrape_yfinance()
        sq.put((bbc_list, yfinance_list))
        time.sleep(3600)

def thread2():
    global test
    while True:
        data_list = []
        with open("user_stock", "rb") as f:
            try:
                while True:
                    data = pickle.load(f)
                    data_list.append(data)
            except EOFError:
                pass
        f.close()

        for data in data_list:
            for ticker, dict_ in data.items():
                curr_price = stock.Stock(ticker).getCurrentPrice()

                curr_total = curr_price*dict_["Count"]
                cost = dict_["Count"]*dict_["Bought Price"]

                gain = round((curr_total - cost)/curr_total, 2)
                dict_["Gain"] = gain

        with open("user_stock", "wb") as f:
            for i in data_list:
                pickle.dump(i, f)
        f.close()

        stock_updated.set()
        time.sleep(10)


def thread3(aq):
    assets = {
        "home": "C:/Users/Harold Indra/Desktop/Coding/Compsci IA/compsci-ia/assets/icons/home.png",
        "search": "C:/Users/Harold Indra/Desktop/Coding/Compsci IA/compsci-ia/assets/icons/search.png",
        "bookmark": "C:/Users/Harold Indra/Desktop/Coding/Compsci IA/compsci-ia/assets/icons/bookmark.png",
        "learning": "C:/Users/Harold Indra/Desktop/Coding/Compsci IA/compsci-ia/assets/icons/learning.png",
        "logout": "C:/Users/Harold Indra/Desktop/Coding/Compsci IA/compsci-ia/assets/icons/logout.png",
        "add": "C:/Users/Harold Indra/Desktop/Coding/Compsci IA/compsci-ia/assets/icons/plus.png"
    }
    aq.put(assets)



if __name__ == "__main__":
    # Multiprocess both the news and stock updates
    main_thread = threading.Thread(target=main, args=(news_queue, asset_queue, stock_updated,))
    news_scrape_thread = threading.Thread(target=thread1, args=(news_queue,))
    update_stock_thread = threading.Thread(target=thread2)
    asset_thread = threading.Thread(target=thread3, args=(asset_queue,))

    main_thread.start()
    news_scrape_thread.start()
    update_stock_thread.start()
    asset_thread.start()