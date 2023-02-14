import loginPage
import homePage
import scraper
import schedule
import multiprocessing
from stock import InputStock

# This is the file the user runs

# In order to update the news display, some functions need to run in the background
# Therefore, the multiprocessing library cajn be used to simultaneously run both the main and sub functions
def multithreading_scraping():
    bbc_scraping = multiprocessing.Process(target=scraper.scrape_bbc)
    yfinance_scraping = multiprocessing.Process(target=scraper.scrape_yfinance)

    bbc_display = multiprocessing.Process(target=homePage.HomePage.display_bbc_headlines)
    yfinance_display = multiprocessing.Process(target=homePage.HomePage.display_yfinance_headlines)

    bbc_scraping.start()
    yfinance_scraping.start()

    bbc_scraping.join()
    yfinance_scraping.join()
        

    bbc_display.start()
    yfinance_display.start()

    bbc_display.join()
    yfinance_display.join()

def main():
    app = loginPage.LoginPage()
    app.mainloop()

if __name__ == "__main__":
    # Multiprocess both the news and stock updates
    schedule.every(1).hour.do(multithreading_scraping)
    schedule.every(1).hour.do(InputStock.multithreading_stock)
    main()