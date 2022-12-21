with open("dayTwoData.txt", "r") as elfData:
	lines = elfData.readlines()

opponentScores = {
    "A":1,
    "B":2,
    "C":3
}

myScores = {
    "X":1,
    "Y":2,
    "Z":3
}

total = 0
#for i in range(5):
for game in lines:
    #game = lines[i]
    game = game.replace('\n', '')
    picks = game.split(' ')
    opponentScore = opponentScores[picks[0]]
    myScore = myScores[picks[1]]
    total += myScore
    if opponentScore == myScore:
        total += 3
    elif opponentScore == 3:
        if myScore == 1:
            total +=  6
    elif opponentScore + 1 == myScore:
        total += 6
    print(f'{game}\t{opponentScore}\t{myScore}\t{total}')
print(total)

QGFsbGVuaG9sdWJAbXN0ZG4uc29jaWFs
