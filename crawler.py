import requests
import url_manager
from bs4 import BeautifulSoup

def tree_spider(max_pages, product):
    page = 1

    product = url_manager.urlify(product)

    while page <= max_pages:
        #Grab Page Source
        url = ('https://www.gumtree.com.au/s-%s/page-%s/k0?fromSearchBox=true' % (product, str(page)))
        source = requests.get(url)
        plain_text = source.text

        #New BeautifulSoup Object
        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.findAll('span', {'itemprop': 'name'}):
            title = link.string
            href = 'https://www.gumtree.com.au' + link.parent.get('href')

            print(title.lstrip())
            get_ad_data(href)

        page += 1

def get_ad_data(ad_url):
    source = requests.get(ad_url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    found_price = soup.find('span', {'class': 'j-original-price'})

    if found_price is None:
        print("Could not fetch price")
    else:
        for ad_price in found_price:
            print(str(ad_price.string).lstrip())

def main():
    search = input("What would you like to search for on Gumtree?\n")
    pages = input("How many pages would you like to crawl?\n")

    tree_spider(int(pages), search)

if __name__ == '__main__':
    main()