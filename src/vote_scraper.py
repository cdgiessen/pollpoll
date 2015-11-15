from bs4 import BeautifulSoup
from urllib2 import urlopen
import sys
max_pages = 1
BASE_WEB_URL = "http://projects.washingtonpost.com/congress/members/"
PARTICULAR_URL = "http://projects.washingtonpost.com/congress/members/"
d = dict()

#Makes Soup from Url
def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")



#Main
def main(input_ID):
    PARTICULAR_URL = BASE_WEB_URL + input_ID + "/votes/"
    PAGE_URL = BASE_WEB_URL + input_ID + "/votes/"
    key_count = 0
    pagelist = soup.find("dev", "pagination wpni-common-pagination")
    for li in pagelist.findall("li"):
        li.a
