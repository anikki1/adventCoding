with open("dayOneData.txt", "r") as elfData:
	lines = elfData.readlines()
elfFood = []
for x in lines: 
    x = x.replace('\n', '')
    if x.isnumeric(): 
        elfFood[-1].append(int(x))
        #print(x)
    else:
        elfFood.append([])
        #print("newElf")
totalFoodPerElf= []
for y in elfFood:
    totalFoodPerElf.append(sum(y))
    #print(len(y))
totalFoodPerElf.sort(reverse=True)
print(totalFoodPerElf[0])

topThreeElves = totalFoodPerElf[0:3]
print(sum(topThreeElves))

