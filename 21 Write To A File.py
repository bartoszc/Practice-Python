import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, features='html.parser')

name = input('Enter the name of the file: ')
name += '.txt'

with open(name, 'w') as open_file:
    for hit in soup.findAll(attrs={'class': 'content-section'}):
        open_file.write(hit.get_text() + '\n')





