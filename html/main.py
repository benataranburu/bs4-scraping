from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

#load soup
try:
    src = urlopen('https://bbc.co.uk/news').read()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    #parse
    content = BeautifulSoup(src,'lxml')

    #read all pharagraphs
    for paragraph in content.find_all('p'):
        print(str(paragraph.text))
