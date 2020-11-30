import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    searchterm = 'sony+a7'
    url = f"https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw='{searchterm}'&_sacat=31388&LH_TitleDesc=0&LH_Sold=1&LH_Complete=1&_ipg=200&rt=nc&LH_Auction=1&_ipg=200"
    soup = get_data(url)
    products = parse(soup)
    export(products)

def get_data(url):
    r = requests.get(url)
    if r.status_code != 200:
        print('Failed to get data: ', r.status_code)
    else:
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.title.text)
    return soup

def parse(soup):
    productlist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    for item in results:
        products = {
        'title': item.find('h3', {'class':'s-item__title s-item__title--has-tags'}).text,
        'soldprice': float(item.find('span', {'class':'s-item__price'}).text.replace('£','').replace(',','').strip()),
        'solddate': item.find('span', {'class': 's-item__title--tagblock__COMPLETED'}).find('span', {'class':'POSITIVE'}).text,
        'bids': item.find('span', {'class': 's-item__bids'}).text,
        'link': item.find('a', {'class': 's-item__link'})['href']        
        }
        productlist.append(products)
        #print(products)
    return productlist

def loadup(productlist):
    return

def export(productlist):
    productsdf = pd.DataFrame(productlist)
    productsdf.to_csv('testoutput.csv', index=False)
    print('Saved to CSV')
    return


if __name__ == '__main__':
    main()

