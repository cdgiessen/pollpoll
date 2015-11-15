from urllib2 import urlopen
import re

def get_member_links(section_url):
    html = urlopen(section_url).read()
    member_dictionary = dict()
    regex = re.findall('[A-Z][0-9]{6}(?=">).*(?=</a>)', html)
    split_list = [ex.split('">') for ex in regex]
    for st in split_list:
        member_dictionary[st[1]] = st[0]
    return member_dictionary

def get_full_member_links():
    full_dict = get_member_links("http://projects.washingtonpost.com/congress/113/house/members/")
    full_dict.update(get_member_links("http://projects.washingtonpost.com/congress/113/senate/members/"))
    return full_dict

def get_member_names():
    full_dict = get_full_member_links()
    return full_dict.keys()
