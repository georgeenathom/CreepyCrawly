import requests
from bs4 import BeautifulSoup

url = 'https://soundcloud.com/'

def creep():
    source_code = requests.get(url)
    base_text = source_code.text
    soup = BeautifulSoup(base_text)

    for link in soup.find_all('a', href=True):
        href = link.get('href')

        print (href)

creep()

