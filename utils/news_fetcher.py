import requests
from bs4 import BeautifulSoup

def fetch_ngx_news():
    url = "https://ngxgroup.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_items = []
    for item in soup.select('.news-item')[:5]:
        title = item.get_text(strip=True)
        link = item.find('a')['href']
        news_items.append({'title': title, 'link': link})

    return news_items
