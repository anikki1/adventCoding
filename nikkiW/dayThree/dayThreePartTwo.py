from itertools import islice
with open('dayThreeData.txt') as file:
    while True:
        next_n_lines = list(islice(file, 3))
        if not next_n_lines:
            break
        # process next_n_lines
aValue = ord('a')
AValue = ord('A')
totalValue = 0
for x in next_n_lines:
    priority = []
    x = x.replace('\n', '')
    aValue = ord('a')
    AValue = ord('A')
    totalValue = 0
    if y not in priority:
     priority.append(y)
    if y.islower():
        totalValue += ord(y) - aValue + 1
    else: 
        totalValue += ord(y) - AValue + 27
print(totalValue)