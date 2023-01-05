from itertools import islice
with open('./dayThreeData.txt') as file:
    totalValue = 0
    aValue = ord('a')
    AValue = ord('A')
    
    while True:
        next_n_lines = list(islice(file, 3))
        if not next_n_lines:
            break
        # process next_n_lines
        #print(next_n_lines[1])
        first = next_n_lines[0]
        second = next_n_lines[1]
        third = next_n_lines[2]
        #print(third)
        for y in first:
          if y in second: 
            if y in third:
                if y.islower():
                    totalValue += ord(y) - aValue + 1
                else: 
                    totalValue += ord(y) - AValue + 27
                break
    print(totalValue)
