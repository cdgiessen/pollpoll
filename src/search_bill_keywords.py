import re

def select_bills2(dictionary, string = ""):
    #looks through the dict and checks to see if any of them don't have the keyword.

    if string == "":
        return dictionary
    else:
        #stringList = string.split() #if string is not a single word
        newList = {}


        for value in range(0,len(dictionary)):
            allRelevant = False
            
            #for stringValue in range(0,len(stringList)):
            #    p = re.compile(stringList[stringValue])
            #    if p.search(dictionary[value][3]) != None:
            #        allRelevant = True
                    
            #if allRelevant:
            #    newList[value] = dictionary[value]

            if re.match(string, dictionary[value][3], re.IGNORECASE) != None:
                newList[value] = dictionary[value]

        return newList

def select_bills(dictionary, string = ""):
    newDict = dict()
    sList = string.split('\s')
    for st in sList:
        p = re.compile(st, re.IGNORECASE)
        for i in dictionary:
            if p.match(dictionary[i][3]) != None:
                newDict[i] = dictionary[i]
    return newDict
