# James Mathew
# CPSC3400
# hw1.py

import sys

def countPairs(fileName):
    pairsOfLetters = {}
    print(pairsOfLetters)
    with open(fileName, 'r') as inputFile:
        # print(inputFile.readline()) 
        for line in inputFile:
            print(line, end = "")
            # print(len(line))
            for x in range(0, (len(line)-2)):
                if pairsOfLetters.get(line[x : x+2]) == None:
                    pairsOfLetters[line[x : x+2]] = 1
                # print(pairsOfLetters[line[x : x+2]])
                # if pairsOfLetters[line[x : x+2]] > 0:
                #     pairsOfLetters[line[x : x+2]] = pairsOfLetters[line[x : x
                    # +2]] + 1
                else:
                    pairsOfLetters[line[x : x+2]] = pairsOfLetters[line[x : 
                            x+2]] + 1
    print(pairsOfLetters)            
                

print('okay')
inputs = sys.argv
print('here')
print(inputs[0])
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
