from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

BASE_URL = "http://projects.washingtonpost.com/"

def get_member_links(section_url):
    html = urlopen(section_url).read()
    return html

get_member_links("http://projects.washingtonpost.com/congress/113/house/members/")
