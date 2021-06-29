import requests
from bs4 import BeautifulSoup
from lxml import html


baseurl = 'https://www.jegs.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
}

productlinks = []

for x in range(1, 2):
    r = requests.get(f'https://www.jegs.com/webapp/wcs/stores/servlet/SearchResultsPageCmd?q=black&pageSize=30&Tab=SKU&storeId=10001&catalogId=10002&langId=-1&pageNumber{x}')
    soup = BeautifulSoup(r.content, 'lxml')
    productlist = soup.find_all('div', id='product-title-wrap')
    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])
print((productlinks))
