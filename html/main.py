import bs4 as bs
import urllib.request

#load soup
src = urllib.request.urlopen('https://bbc.co.uk/news').read()
#parse
content = bs.BeautifulSoup(src,'lxml')

#read all pharagraphs
for paragraph in content.find_all('p'):
    print(str(paragraph.text))
