import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features='html.parser')

for hit in soup.findAll(attrs={'class': 'content-section'}):
    print(hit.text.strip())
