from itertools import islice
with open('dayThreeData.txt') as file:
    while True:
        next_n_lines = list(islice(file, 3))
        if not next_n_lines:
            break
        # process next_n_lines
        #print(next_n_lines[1])
        aValue = ord('a')
        AValue = ord('A')
        totalValue = 0
    for x in next_n_lines:
        priority = []
        x = x.replace('\n', '')
        first = next_n_lines[0]
        second = next_n_lines[1]
        third = next_n_lines[2]
        #print(third)
        for y in first:
          if y in second: 
            if y in third:
                if y not in priority:
                    priority.append(y)
                if y.islower():
                    totalValue += ord(y) - aValue + 1
                else: 
                    totalValue += ord(y) - AValue + 27
print(totalValue)


