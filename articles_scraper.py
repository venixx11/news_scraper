import requests
from bs4 import BeautifulSoup


news_url = 'https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/'

r = requests.get(news_url)

soup = BeautifulSoup(r.content, 'html.parser')
paragraphs = soup.find('article')
print(paragraphs.text)
