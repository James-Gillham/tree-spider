import requests
from bs4 import BeautifulSoup

def creepy_crawler(max_pages, product):
    page = 1

    while page <= max_pages:
        #Grab Page Source
        url = ('https://www.gumtree.com.au/s-%s/page-%s/k0?fromSearchBox=true' % (product, str(page)))
        source = requests.get(url)
        plain_text = source.text

        #New BeautifulSoup Object
        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.findAll('span', {'itemprop': 'name'}):
            title = link.string

        page += 1

def get_ad_data(ad_url):
    


creepy_crawler(1, 'bananas')