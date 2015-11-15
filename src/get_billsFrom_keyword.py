import re

def selectBills(dict, string = ""):
    #looks through the dict and checks to see if any of them don't have the keyword.
    if string == "":
        return dict
    else:
        newList = {}
        p = re.compile(string)
        for value in range(0,len(dict)):
            if p.search(dict[value][3]) != None:
                newList[value] = dict[value]
        return newList

