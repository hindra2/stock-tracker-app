import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news/business"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all the headline elements on the page
headlines = soup.find_all("a", class_="gs-c-promo-heading")

# Extract the text and link of each headline
for i, headline in enumerate(headlines[:10]):
    text = headline.text
    link = headline["href"]
    print(f"{i+1}. {text} ({link})")