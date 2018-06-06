import bs4 as bs
import urllib.request

src = urllib.request.urlopen('https://bbc.co.uk/news').read()

content = bs.BeautifulSoup(src,'lxml')

for paragraph in content.find_all('p'):
    print(str(paragraph.text))
