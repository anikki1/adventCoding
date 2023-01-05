with open("dayFourData.txt", "r") as rpsData:
	lines = rpsData.readlines()

totalRanges = 0

for x in lines:
    x = x.replace('\n', '')
    separator = x.split(",")
    #splitting each line's arrays into first and last numbers
    splitFirstSet = separator[0].split("-")
    splitSecondSet = separator[1].split("-")
    
    #converting into integers
    firstSetZero = int(splitFirstSet[0])
    firstSetOne = int(splitFirstSet[1])
    secondSetZero = int(splitSecondSet[0])
    secondSetOne = int(splitSecondSet[1])

    #if else statement to figure out if range A is COMPLETELY in range B or vice versa
    #if (firstSetZero <= secondSetZero) and (firstSetOne >= secondSetOne):
    #    totalRanges += 1
    #elif (secondSetZero <= firstSetZero) and (secondSetOne >= firstSetOne):
    #    totalRanges +=1
    

    #if else statement to figure out if either range overlaps at all
    if (firstSetZero >=secondSetZero and firstSetZero <=secondSetOne):
        totalRanges+=1
    elif(firstSetOne >=secondSetZero and firstSetOne <=secondSetOne):
        totalRanges+=1
    elif(secondSetZero >= firstSetZero and secondSetZero <= firstSetOne):
        totalRanges+=1
    elif(secondSetOne >= firstSetZero and secondSetOne <= firstSetOne):
        totalRanges+=1
print(totalRanges)


#for x in range(5,17):
 #   print(x)


