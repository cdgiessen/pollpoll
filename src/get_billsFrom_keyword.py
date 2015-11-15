import re

#myDict = {0:["","","","hello"],1:["","","","hello world"],2:["","","","yeahno"]}

#def main():
#    print(selectBills(myDict,["world","yeahno"]))

def selectBills(dict, stringList):
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

#if __name__ == "__main__":
#    main()