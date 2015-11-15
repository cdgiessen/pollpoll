from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

dictionary_index = 0
BASE_WEB_URL = "http://projects.washingtonpost.com/congress/members/"
PARTICULAR_URL = "http://projects.washingtonpost.com/congress/members/"
d = dict()

#Get Maximum number of pages to iterate through
def get_max_pg(PAGE_URL):
    html = urlopen(PAGE_URL).read()
    regex = re.findall('(?<=page)[0-9]+', html)
    max_pg =0
    for i in regex:
        if int(i) > max_pg:
            max_pg = int(i)
    return max_pg

#Iterate through Each Page and add to Dict
def pg_by_pg():
    halp = 0

#description Get
def description_get(in_str):
    str3 = re.findall('(?=md-gray">).*(?=</p>)', in_str, re.DOTALL)
    strl3 = str3[0].split(">", 1)
    return (strl3[1])

#Name Get
def name_get(in_str):
    sen = []# = re.findall('[A-Z] [0-9]{3,4}', in_str, re.DOTALL)
    rep = re.findall('[A-Z] [A-Z]{0,3}[0-9]{3,4}', in_str, re.DOTALL)
    if sen != []:
        return sen[0]
    if rep != []:
        return rep[0]
    return "N/A"

#Voted
def voted_get(in_str):
    strV = re.findall('(?=vote-).*',in_str)
    return strV[0]

#Passed
def passed_get(in_str):
    strV = re.findall('(?=assed).*(?<=</span>)',in_str)
    print(strV)
    strP = strV[0].split(">" , 1)
    strP2 = strP[1].split("<",1)
    return strP2[0]


#Scans Page
def scan_page(PAGE_URL):
    html = urlopen(PAGE_URL).read()
    regex = re.findall('(?<=VOTE ROW).*(?=END VOTE ROW)', html, re.DOTALL)
    str1 = regex[0]
    regex2 = re.findall('(?<=<tr>).*(?=</tr>)',str1,re.DOTALL)
    strlist = regex2[0].split("</tr>", 10)
    for str in strlist:
        #print("\nSTRING: \n")
        
        #print(str)

        #Info Get
        print("\nDescript: \n")
        descript = description_get(str)
        print(descript)
        print("\nName: \n")
        name = name_get(str)
        print(name)
        print("\nVoted: \n")
        voted = voted_get(str)
        print(voted)
        print("\nPassed: \n")
        passed = passed_get(str)
        print(passed)
        #if passed == "Failed" or passed == "Passed":
         #   d[dictionary_index] = [name,voted,passed,descript]
          #  dictionary_index = dictionary_index + 1



#Main
def main(input_ID):
    PARTICULAR_URL = BASE_WEB_URL + input_ID + "/votes/"
    PAGE_URL = BASE_WEB_URL + input_ID + "/votes/"
    print(PARTICULAR_URL)
    max_pg = get_max_pg(PAGE_URL)
    scan_page(PAGE_URL)
    print(d)

if __name__ == "__main__":
    main("A000369")
