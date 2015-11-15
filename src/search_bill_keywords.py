import re

def select_bills(dictionary, string = ""):
    #looks through the dict and checks to see if any of them don't have the keyword.

    if string == "":
        return dictionary
    else:
        #stringList = string.split() #if string is not a single word
        newList = {}

        p = re.compile(string)

        for value in range(0,len(dictionary)):
            allRelevant = False
            
            #for stringValue in range(0,len(stringList)):
            #    p = re.compile(stringList[stringValue])
            #    if p.search(dictionary[value][3]) != None:
            #        allRelevant = True
                    
            #if allRelevant:
            #    newList[value] = dictionary[value]

            if re.match(p, dictionary[value][3], re.IGNORECASE) != None:
                print "poop"
                newList[value] = dictionary[value]

        return newList
