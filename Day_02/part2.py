file = open("input.txt", "r")
rpsDic = {"rock": ["paper", 1], "paper": ["scissors", 2], "scissors": ["rock", 3]}
score = 0
for line in file:
    lineTab = line\
        .replace("\n", "")\
        .replace("A", "rock")\
        .replace("B", "paper")\
        .replace("C", "scissors")\
        .split(" ")

    if lineTab[1] == "X":
        #Bruh
        score += rpsDic[rpsDic[rpsDic[lineTab[0]][0]][0]][1]
    elif lineTab[1] == "Y":
        score += 3
        score += rpsDic[lineTab[0]][1]
    else:
        score += 6
        score += rpsDic[rpsDic[lineTab[0]][0]][1]

print(score)