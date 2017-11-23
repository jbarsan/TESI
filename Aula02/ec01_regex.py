import re
from crawler import download

url = 'http://example.webscraping.com/places/default/view/United-Kingdom-239'
page = download(url)
area = re.findall(r'<td class="w2p_fw">(.*?)</td>', page)[1]
print(area)