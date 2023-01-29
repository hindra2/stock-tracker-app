import requests
from bs4 import BeautifulSoup

def scrape():
    url = "https://www.bbc.com/news/business"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines_dict = {}

    headlines = soup.find_all("a", class_="gs-c-promo-heading")

    for i, headline in enumerate(headlines[:10]):
        text = headline.text
        link = headline["href"]
        headlines_dict[i] = [text, f"https://www.bbc.com{link}"]

    return headlines_dict