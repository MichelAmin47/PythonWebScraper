from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html5lib')
        page_title = bs.body.h1
    except AttributeError as e:
        return None
    return page_title


title = get_title('http://www.pythonscraping.com/pages/page1.html')
if title is None:
    print("Title could not be found")
else:
    print(title)
