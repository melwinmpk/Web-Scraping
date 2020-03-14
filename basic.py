from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
''' This Code is all about getting links in <a> tag getting href data storing in a csv file '''
my_url = "https://www.rirm.in"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
links = page_soup.findAll("a")

filename = "links.csv"
f = open(filename,"w")
headers="Links\n"
f.write(headers)
for link in page_soup.findAll("a", attrs={'href': re.compile("")}):
    f.write(link.get('href')+"\n")
    # print(link.get('href'))

f.close()

