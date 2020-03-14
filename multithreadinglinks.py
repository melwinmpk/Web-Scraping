from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
# import linksfunction.getlinks
import re
from threading import Thread
import urllib

my_url = "https://www.toprankers.com"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
links = page_soup.findAll("a")

filename = "links.csv"
f = open(filename,"w")
headers="Links\n"
f.write(headers)

def getlinks(my_url):
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    links = page_soup.findAll("a")
    list_link = []
    for link in page_soup.findAll("a", attrs={'href': re.compile("")}):
        list_link.append(link.get('href'))
        f.write(link.get('href') + "\n")
    return list_link

for link in page_soup.findAll("a", attrs={'href': re.compile("^https")}):
    t = Thread(target=getlinks, args=(link.get('href'),))
    t.start()


