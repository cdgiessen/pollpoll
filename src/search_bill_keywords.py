import re

def select_bills(dictionary, string = ""):
    newDict = dict()
    sList = string.split('\s')
    
    for i in dictionary:
        for st in sList:
            s = str(st)
            if s in str(dictionary[i][4]):
                newDict[i] = dictionary[i]
                print newDict[i]
                print dictionary[i]
    return newDict
