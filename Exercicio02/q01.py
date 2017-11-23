from bs4 import BeautifulSoup
from urllib.request import urlopen
from crawler import download

url = 'https://www.rottentomatoes.com/browse/tv-list-1'
html = download(url)
soup = BeautifulSoup(html, 'html5lib')
tr = soup.find_all('tr', class_=('tv_show_tr tvTopListTitle'))


for i in tr:
    print(i.get_text().strip())
    print('*----------------*')