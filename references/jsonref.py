import requests
from bs4 import BeautifulSoup

url = "https://www.investopedia.com/news/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup)

headlines_dict = {}

headlines = soup.find_all("a", class_="title")

for i, headline in enumerate(headlines[:10]):
    text = headline.text
    link = headline["href"]
    headlines_dict[i] = [text, link]

print(headlines_dict)