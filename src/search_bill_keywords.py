import re

def select_bills(dictionary, string = ""):
    #looks through the dict and checks to see if any of them don't have the keyword.

    if string == "":
        return dictionary
    else:
        stringList = string.split()
        newList = {}
        
        for value in range(0,len(dictionary)):
            allRelevant = False
            
            for stringValue in range(0,len(stringList)):
                p = re.compile(stringList[stringValue])
                if p.search(dictionary[value][3]) != None:
                    allRelevant = True
                    
            if allRelevant:
                newList[value] = dictionary[value]
        return newList
