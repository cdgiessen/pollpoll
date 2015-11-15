import re

def select_bills(dict, stringList):
    #looks through the dict and checks to see if any of them don't have the keyword.
    if len(stringList) == 0:
        return dict
    else:
        newList = {}
        
        for value in range(0,len(dict)):
            allRelevant = False
            
            for stringValue in range(0,len(stringList)):
                p = re.compile(stringList[stringValue])
                if p.search(dict[value][3]) != None:
                    allRelevant = True
                    
            if allRelevant:
                newList[value] = dict[value]
        return newList
