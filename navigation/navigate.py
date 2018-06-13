import bs4 as bs
import urllib.request

#load soup
try:
    src = urllib.request.urlopen('https://www.bbc.co.uk/news').read()
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    #parse
    content = bs.BeautifulSoup(src,'lxml')

    # find occurrences of a certain class
    print("BBC News: Latest headlines:")
    h3 = content.find('h3','gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')
    p = content.find('p','gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary')
    if h3.text is not None and p.text is not None:
        print(h3.text + ": " + p.text)
    else:
        print("not found")
