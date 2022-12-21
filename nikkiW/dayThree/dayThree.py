with open("dayThreeData.txt", "r") as bagData:
	#lines = [line for line in bagData][:3]
    lines = bagData.readlines()


aValue = ord('a')
AValue = ord('A')
totalValue = 0
for x in lines:
    priority = []
    x = x.replace('\n', '')



    halfLength = int((len(x)/2))
    first = x[0:halfLength]
    second = x[halfLength:]
    #print(f'{halfLength}\t{x}\t{first}\t{second}')
    for y in first: 
        if y in second:
            if y not in priority:
                priority.append(y)
                if y.islower():
                    totalValue += ord(y) - aValue + 1
                else: 
                    totalValue += ord(y) - AValue + 27
                #print(f'{y}\t{ord(y) - AValue + 27}')
print(totalValue)




