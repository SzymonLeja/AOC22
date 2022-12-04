file = open("input.txt", "r")

score = 0
secondScore = 0
for line in file:
    lineTab = line.split(",")
    first, second = lineTab[0].split("-"), lineTab[1].split("-")
    firstTab, secondTab = set(list(range(int(first[0]), int(first[1]) + 1))), set(
        list(range(int(second[0]), int(second[1]) + 1)))
    if set(firstTab).issubset(secondTab) or set(secondTab).issubset(firstTab):
        score += 1
    if len(firstTab.intersection(secondTab)) > 0:
        secondScore += 1

print(score)
print(secondScore)
