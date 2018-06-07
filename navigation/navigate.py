import bs4 as bs
import urllib.request

#load soup
src = urllib.request.urlopen('https://www.bbc.co.uk/news').read()
#parse
content = bs.BeautifulSoup(src,'lxml')

# find occurrences of a certain class
for h3 in content.find_all('h3','gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text'):
    print(h3.text)
