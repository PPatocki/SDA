from datetime import datetime
t = datetime.now()
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.imdb.com')
page = BeautifulSoup(response.content, 'html.parser')
BASE_URL = 'https://www.imdb.com'

linki = []
for url in page.find_all('a'):
    if 'marvel' in url.get_text().lower():
        linki.append(BASE_URL + url.get('href'))


print(datetime.now() - t)
print(linki)



#print(response)
