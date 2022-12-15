with open("dayTwoData.txt", "r") as rpsData:
	lines = rpsData.readlines()
#setting up dictionaries 
#playValues = {
#    "A":1,
#    "B":2,
#    "C":3,
#    "X":1,
#    "Y":2,
#    "Z":3
#}
totalPoints = 0
for turn in lines: 
    turn = turn.replace('\n', '')
    plays = turn.split(" ")

    #part one attempt 
 #   opponent = playValues[plays[0]]
 #   me = playValues[plays[1]]
 #   #setting up the comparison between me and opponent (no assignment for value itself for me)
 #   if opponent == me: 
 #       totalPoints += 3
 #   elif opponent == 1 and me == 2:
 #       totalPoints += 6
 #   elif opponent == 2 and me == 3:
 #       totalPoints +=6
 #   elif opponent == 3 and me == 1:
 #       totalPoints +=6
 #   totalPoints += me
 #   print(totalPoints)
# --- Part Two ---
#
#The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
#
#The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:
#
#In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
#In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
#In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
#Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
#
#Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
#
   #if opponent is rock
    if plays[0] == 'A' and plays[1] =='Y':
        totalPoints += 4
    elif plays[0] == 'A' and plays[1] == 'X':
        totalPoints += 3
    elif plays[0] == 'A' and plays[1] == 'Z':
        totalPoints += 8
    #if opponent is Paper
    if plays[0] == 'B' and plays[1] =='X':
        totalPoints += 1
    elif plays[0] == 'B' and plays[1] == 'Y':
        totalPoints += 5
    elif plays[0] == 'B' and plays[1] == 'Z':
        totalPoints += 9
    #if opponent is Scissors
    if plays[0] == 'C' and plays[1] =='X':
        totalPoints += 2
    elif plays[0] == 'C' and plays[1] == 'Y':
        totalPoints += 6
    elif plays[0] == 'C' and plays[1] == 'Z':
        totalPoints += 7
    print(totalPoints)
    
    
    

    



    




