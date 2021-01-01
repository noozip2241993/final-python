textFile = open("alice.txt", "r")
textData = textFile.read()

myDict = {}
frequencyDict = {}
lineCount = 1
for line in textData.split("\n"):
    
    #print(line.split(" "))
    for word in line.split(" "):
        print(word) 
        if word in myDict.keys():
            myDict[word] = myDict[word] + str(lineCount)
        else:
            myDict[word] = str(lineCount)

        if word in frequencyDict.keys():
            frequencyDict[word] = int(frequencyDict[word]) + 1
        else:
            frequencyDict[word] = 1
    lineCount = lineCount + 1

print(myDict)
print(frequencyDict)

textFile.close()

outputFile = open('index.txt', 'w+')

for key in sorted(myDict.keys()):
    frequency = frequencyDict[key]
    lines = " ".join(myDict[key]) 
    displayVal = (f'{key:<13} ({frequency}): {lines}\n')
    outputFile.write(displayVal)
outputFile.close()

