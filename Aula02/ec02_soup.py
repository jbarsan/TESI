from bs4 import BeautifulSoup
from crawler import download

url = 'http://example.webscraping.com/places/default/view/United-Kingdom-239'
html = download(url)
soup = BeautifulSoup(html, 'html.parser')
tr = soup.find(attrs={'id': 'places_area__row'})
td = tr.find(attrs={'class': 'w2p_fw'})
area = td.text
print(area)