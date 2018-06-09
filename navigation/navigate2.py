import bs4 as bs
import urllib.request

#load soup
src = urllib.request.urlopen('https://flights.ryanair.com/es-es/vuelos-a-londres').read()
#parse
content = bs.BeautifulSoup(src,'lxml')

# find ocurrences of a certain class
for deal in content.find_all('h1'):
    print('Oferta: ' + deal.text)
