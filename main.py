import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/all/'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')

for article in articles:
    title_tag = article.find('h2')

    if not title_tag:
        continue

    title = title_tag.get_text(strip=True)

    link_tag = title_tag.find('a')

    if not link_tag:
        continue

    link = link_tag.get('href')

    if not link:
        continue

    time_tag = article.find('time')

    if not time_tag:
        continue

    date = time_tag.get('datetime') or time_tag.get_text(strip=True)

    preview = article.get_text(separator=' ', strip=True)

    if any(word.lower() in preview.lower() for word in KEYWORDS):
        if link.startswith('/'):
            link = 'https://habr.com' + link

        print(f'{date} – {title} – {link}')
