import requests
from modules import url_manager
from bs4 import BeautifulSoup

def tree_spider(max_pages, product):
    page = 1

    product = url_manager.urlify(product)	#adjust user input to Gumtree url-friendly input

    while page <= max_pages:
        #Grab Page Source
        url = ('https://www.gumtree.com.au/s-%s/page-%s/k0?fromSearchBox=true' % (product, str(page)))
        source = requests.get(url)
        plain_text = source.text

        #New BeautifulSoup Object
        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.findAll('span', {'itemprop': 'name'}):		#find the name tag in Gumtree search
            title = link.string
            href = 'https://www.gumtree.com.au' + link.parent.get('href')	#also grab the url

            print("-----------------------------------------\n" + title.lstrip().rstrip())	#formatting

            get_ad_data(href)	#pass the url on to grab price/location later

        page += 1

def get_ad_data(ad_url):
    source = requests.get(ad_url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, 'html.parser')

    found_price = soup.find('span', {'class': 'j-original-price'})	#find the price tag

    if found_price is None:
        print("Could not fetch price\n" + "-----------------------------------------\n") #some ads on Gumtree don't have price listings
    else:
        for ad_price in found_price:
            print(str(ad_price.string).lstrip())	#print the price with some formatting
    print("-----------------------------------------\n")


def check_entries(search, pages):
    #Poorly planned query validation

    search = str(search)
    search.strip("\'")	#removing '
    if not search.isalnum():	#check for alphanumeric
        search = ""

    if not pages.isnumeric():
        pages = 1

    tree_spider(int(pages), search)


def main():
    search = input("What would you like to search for on Gumtree?\n")	#gather user inputs
    pages = input("How many pages would you like to crawl?\n")

    check_entries(search, pages)

if __name__ == '__main__':
    main()