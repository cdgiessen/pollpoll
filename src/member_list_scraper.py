from urllib2 import urlopen
import re

def get_member_links(section_url):
    html = urlopen(section_url).read()
    
    regex = re.findall('[A-Z][0-9]{6}(?=">).*(?=</a>)', html)
    split_list = [ex.split('">') for ex in regex]
    for st in split_list:
        print st
    return "top kek"

print get_member_links("http://projects.washingtonpost.com/congress/113/house/members/")
