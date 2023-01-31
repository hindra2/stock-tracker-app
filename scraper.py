import requests
from bs4 import BeautifulSoup

def scrape(url, html, class_, source):
    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.text, "html.parser")

    headlines = set()

    scraped_headlines = soup.find_all(html, class_=class_)

    for i, headline in enumerate(scraped_headlines[:10]):
        text = headline.text
        link = headline["href"]
        if text in headlines:
            print(f"{text} already in headlines set")
        else:
            headlines.add((text, f"{source}{link}"))
    
    return headlines

# def scrape_bbc():
#     url = "https://www.bbc.com/news/business"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     headlines = set()

#     scraped_headlines = soup.find_all("a", class_="gs-c-promo-heading")

#     for i, headline in enumerate(scraped_headlines[:10]):
#         text = headline.text
#         link = headline["href"]
#         if text in headlines:
#             print(f"{text} already in headlines set")
#         else:
#             headlines.add((text, f"https://www.bbc.com{link}"))

#     return headlines

# def scrape_goog():