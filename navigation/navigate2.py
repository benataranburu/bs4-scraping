from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

#load soup
try:
    src = urlopen('https://flights.ryanair.com/es-es/vuelos-a-londres').read()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    #parse
    content = BeautifulSoup(src,'lxml')

    # find ocurrences of a certain class
    for deal in content.find_all('h1'):
        print('Oferta: ' + deal.text)
