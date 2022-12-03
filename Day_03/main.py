file = open("input.txt", "r")
sum = 0
for line in file:
    firstpart, secondpart = set(line[:len(line) // 2]), set(line[len(line) // 2:])
    commonSet = set.intersection(firstpart, secondpart)
    chrVal = ord(commonSet.pop())
    if(chrVal>=97):
        sum += (chrVal-96)
    else:
        sum += (chrVal - 38)
print(sum)