from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

#load soup
try:
    src = urlopen('https://www.as.com').read()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    #parse
    content = BeautifulSoup(src,'lxml')

    # find ocurrences of a certain class
    for tag in content.find_all(text=re.compile('Mundial')):
        print(tag)
