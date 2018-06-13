import bs4 as bs
import urllib.request
from urllib.error import HTTPError

#load soup
try:
    src = urllib.request.urlopen('https://bbc.co.uk/news').read()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    #parse
    content = bs.BeautifulSoup(src,'lxml')

    #read all pharagraphs
    for paragraph in content.find_all('p'):
        print(str(paragraph.text))
