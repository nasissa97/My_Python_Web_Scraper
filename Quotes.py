import requests
import bs4

# Goal: grab all the unique authors from http://quotes.toscrape.com/page 

# Code Between """ was dividing my goal into smaller ones
"""
url = 'http://quotes.toscrape.com/page/{}/'
res = requests.get(url.format(1))

soup = bs4.BeautifulSoup(res.text, 'lxml')
#print(soup)

authors = soup.select('.author')
quotes = soup.select('.quote')

#for author in authors:

    #print(author.text)

for quote, author in zip(quotes, authors):
    quote_text = quote.select('span')[0]
    #author = quote.select('span')[1]

    print(quote_text.text)
    print(author.text)
"""
# used set instead of list to prevent dupicates
unique_authors = set()
url = 'http://quotes.toscrape.com/page/{}/'
i = 1
page = True
while(page):
    #only changes to the url is the page number 
    scrape_url = url.format(i)
    #grabs page
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    #print(scrape_url)
    #if .author returns [] then we reached the last page
    if soup.select('.author') == []:
        break
    # Author name is in author class
    authors = soup.select('.author')
    
    for author in authors:
        unique_authors.add(author.text)
    i += 1
for author in unique_authors:
    print(author)

# grab the top ten tags
tags = soup.select('.col-md-4.tags-box span')
for tag in tags:
    print(tag.text)


