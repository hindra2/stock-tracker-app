# Library Imports
import requests
from bs4 import BeautifulSoup

# News class to keep each headline and link pair seperate
class News:
    def __init__(self, headline, url):
        self.headline = headline
        self.url = url

    def return_headline(self):
        return self.headline

    def return_url(self):
        return self.url

# Scrapes headlines from bbc with beatifulsoup4
def scrape_bbc():
    url = "https://www.bbc.com/news/business"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Scrapes all html elements with the "a" tag and class "gs-c-promo-heading"
    scraped_headlines = soup.find_all("a", class_="gs-c-promo-heading")

    headlines = []

    for h3_tag in scraped_headlines:
        headline = h3_tag.text
        link = h3_tag["href"]
        headlines.append((headline, f"https://www.bbc.com{link}"))

    # Returns the first 5 elements of a list
    return headlines[:20]

def scrape_yfinance():
    url = "https://finance.yahoo.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Scrapes all html elements with the "h3" tag
    scraped_headlines =  soup.find_all("h3")

    headlines = []

    for h3_tag in scraped_headlines:
        headline = h3_tag.text
        link = h3_tag.find("a")["href"]
        headlines.append((headline, f"https://finance.yahoo.com{link}"))

    # Returns headlins 6-11 as the first 6 are not news headlines
    return headlines[6:26]