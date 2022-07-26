import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US;q=0.5,en;q=0.3',
    'DNT': '1',
    'Pragma': 'no-cache'
}
url = 'https://habr.com/ru/all/'

response = requests.get(url, headers=HEADERS)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all(class_='tm-article-snippet')
for article in articles:
    for keyword in KEYWORDS:
        if article.text.lower().find(keyword) > 0:
            data = article.find('time').get('title')
            header = article.find('h2').find('span').text
            link = article.find('h2').find('a').get('href')
            print(f'Дата публикации: {data}, Заголовок: {header}. Ссылка: {"https://habr.com" + link}')