import re

def select_bills(dictionary, string = ""):
    newDict = dict()
    sList = string.split('\s')
    
    for st in sList:
        s = str(st)
        p = re.compile(s, re.IGNORECASE)
        for i in dictionary:
            if p.match(dictionary[i][3]) != None:
                newDict[i] = dictionary[i]
    return newDict
