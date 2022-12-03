file = open("input.txt", "r")
rpsDic = {"rock": ["paper", 1], "paper": ["scissors", 2], "scissors" : ["rock", 3]}
score = 0
for line in file:
    lineTab = line\
        .replace("\n", "")\
        .replace("A", "rock")\
        .replace("B", "paper")\
        .replace("C", "scissors")\
        .replace("X", "rock")\
        .replace("Y", "paper")\
        .replace("Z", "scissors")\
        .split(" ")

    if lineTab[0] == lineTab[1]:
        score += 3
    elif lineTab[0] != rpsDic[lineTab[1]][0]:
        score += 6
    score += rpsDic[lineTab[1]][1]
print(score)