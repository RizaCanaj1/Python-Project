import re
import csv
import requests
import json
from bs4 import BeautifulSoup

def get_links(file):
    urls = []
    #all_pages_urls=[]
    with open(file,'r') as fh:
        content = fh.read()
        urls = content.splitlines()
        html = get_html(urls[0])
        soup = BeautifulSoup(html,'html.parser')
        #maxPages= int(soup.select_one('#Catalog > div > div.catalog__display-wrapper.catalog__grid-wrapper > div > small-pagination > div > button:nth-child(4) > span').text)
        #page = 1
        #for i in range(maxPages):
            #page = i+1
            #print(i+1)
            #all_pages_urls.append(url[0]+str(i+1))
    #return [url,page]
    articles = soup.select('div.paginated-products-grid a')
    games_urls = []
    for article in articles:
        games_urls.append(article['href'])
    return games_urls
def get_html(url):
    response = requests.get(url)
    if(response.status_code==200):
        return response.text
    else:
        raise Exception("Error: {response.status_code}")
def scrape(url):
    html = get_html(url)
    soup = BeautifulSoup(html,'html.parser')
    
    span_element = soup.select_one('span.product-actions-price__final-amount _price')
    starting_price = 'Free'
    if span_element is not None:
        starting_price = span_element.text
    images = soup.select('img.productcard-thumbnails-slider__image')
    title = soup.select_one('h1.productcard-basics__title')
    if title is not None:
        title = title.text
    else:
        title = "No title for this Game"
    description = soup.select_one('div.description')
    #return{"title":title,"price":starting_price,"images":images,"description":description,"page":page}
    return{"title":str(title),"price":str(starting_price),"images":str(images),"description":str(description)}
#def scrape_and_store(urls,page):
def get_games(urls):
    games = []
    if len(urls) == 0:
        raise Exception('URLs list is empty!!')
    for url in urls:
        try:
            game = scrape(url)
            games.append(game)
            print('Scraping: ' + game['title'])
        except Exception as e:
            print(e)
    return games
def save_games(games, file):
    if len(games) == 0:
        raise Exception('Post list is empty!')
    with open(file, 'w') as fh:
        json.dump(games, fh)
    print('Done!')

try:
    urls = get_links('scrappedlinks.txt')
    games = get_games(urls)
    save_games(games, 'games.json')
except Exception as e:
    print(e)   
#print(get_games(get_links('scrappedlinks.txt')))