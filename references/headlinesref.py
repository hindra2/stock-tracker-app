import requests
from bs4 import BeautifulSoup


def scrape_yfinance():
    url = "https://finance.yahoo.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    scraped_headlines =  soup.find_all("h3")

    headlines = []

    for h3_tag in scraped_headlines:
        headline = h3_tag.text
        link = h3_tag.find("a")["href"]
        headlines.append([headline, f"https://finance.yahoo.com{link}"])

    return headlines[6:11]

listst = scrape_yfinance()

text = listst[0][0]
link = listst[0][1]