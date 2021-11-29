from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bs = BeautifulSoup(html.read(), 'html5lib')
#
# nameList = bs.findAll('span', {'class': 'green'})
# for name in nameList:
#     print(name.get_text())

html = urlopen('https://www.nike.com/nl/w/heren-jordan-schoenen-37eefznik1zy7ok')
bs = BeautifulSoup(html.read(), 'html5lib')

nameList = bs.findAll('a', {'class': 'product-card__link-overlay'})
for name in nameList:
    print(name.get_text())
