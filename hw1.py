# James Mathew
# CPSC3400
# hw1.py

import sys



def countPairs(fileName):
    pairsOfLetters = {}
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            for x in range(0, (len(line)-2)):
                tempString = line[x : x + 2].lower()
                if tempString.isalpha():
                    if pairsOfLetters.get(tempString) == None:
                        pairsOfLetters[tempString] = 1
                    else:
                        pairsOfLetters[tempString] = pairsOfLetters[tempString] + 1
    return pairsOfLetters



def getTopFivePairs(pairsOfLetters):
    letterPairs = list(pairsOfLetters.items())
    allValues = list(pairsOfLetters.values())
    maxValue = max(allValues)
    preMax = -1
    topFive = []
    counter = 0
    while(len(allValues) !=0 and (counter <= 5 or preMax == maxValue)):
        counter = counter+1
        indx = allValues.index(maxValue)
        topFive.append(letterPairs[indx])
        allValues.pop(indx)
        if len(allValues) != 0:
            letterPairs.pop(indx)
            helpIndx = -1
            while(preMax == maxValue):
                if topFive[helpIndx - 1][0] > topFive[helpIndx][0]:
                    temp = topFive[helpIndx - 1]
                    topFive[helpIndx - 1] = topFive[helpIndx]
                    topFive[helpIndx] = temp
                helpIndx = helpIndx-1
                if (len(topFive) + (helpIndx - 1)) >= 0:
                    preMax = topFive[helpIndx - 1][1]
                else:
                    preMax = -1
            preMax = maxValue
            maxValue = max(allValues)
    return tuple(topFive)


def createFollowDict(pairsOfLetters, letter):
    letter = letter.lower()
    numOfLetters = {}
    for x in range(97,123):
        numOfLetters[chr(x)] = 0
    allKeys = pairsOfLetters.keys()
    for key in allKeys:
        if key[0] == letter:
            numOfLetters[key[1]] = pairsOfLetters[key]
    return numOfLetters    
    



inputs = sys.argv
pairs = countPairs(inputs[1])
print(len(pairs))
allValues = list(pairs.values())
totalPairs = 0
for x in allValues:
    totalPairs = totalPairs + x
print(totalPairs)
topFivePairs = getTopFivePairs(pairs)
print(topFivePairs)

numOfLetters = createFollowDict(pairs, 'A')
numLetters = list(numOfLetters.values())
print('a')
print(numLetters)
numOfLetters = createFollowDict(pairs, 'e')
numLetters = list(numOfLetters.values())
print('e')
print(numLetters)
numOfLetters = createFollowDict(pairs, 'i')
numLetters = list(numOfLetters.values())
print('i')
print(numLetters)
numOfLetters = createFollowDict(pairs, 'o')
numLetters = list(numOfLetters.values())
print('o')
print(numLetters)
numOfLetters = createFollowDict(pairs, 'u')
numLetters = list(numOfLetters.values())
print('u')
print(numLetters)


