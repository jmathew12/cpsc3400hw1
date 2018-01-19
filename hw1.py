# James Mathew
# CPSC3400
# hw1.py

import sys

def countPairs(fileName):
    pairsOfLetters = {}
    # print(pairsOfLetters)
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            # print(line, end = "")
            for x in range(0, (len(line)-2)):
                tempString = line[x : x+2].lower()
                
                if tempString.isalpha():
                    # print(tempString)
                    if pairsOfLetters.get(tempString) == None:
                        pairsOfLetters[tempString] = 1
                    else:
                        pairsOfLetters[tempString] = pairsOfLetters[tempString] + 1
    print(pairsOfLetters)
    return pairsOfLetters



def getTopFivePairs(pairsOfLetters):
    pass

def createFollowDict(pairsOfLetters):
    pass
           
                

# print('okay')
inputs = sys.argv
# print('here')
# print(inputs[0])
countPairs(inputs[1])
 











# with open('sample.txt', 'r') as inputFile:
#     for line in inputFile
#         f_contents = inputFile.readline()
#         print(f_contents)

# print(f.closed)


# print(f.read())

# inputFile = open('sample.txt', 'r')
# f_contents = inputFile.readline()
# print(f_contents)
# inputFile.close()
# print('sample print this baby')
# print(f.mode)
