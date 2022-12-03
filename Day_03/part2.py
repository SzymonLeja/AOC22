file = open("input.txt", "r").read().split()
sum = 0
for r1,r2,r3 in zip(file[0::3],file[1::3],file[2::3]):
    firstSet, secondSet, thirdSet = set(r1), set(r2), set(r3)
    tabOfSets = [firstSet,secondSet,thirdSet]
    commonSet = set.intersection(*map(set,tabOfSets))
    chrVal = ord(commonSet.pop())
    if(chrVal>=97):
        sum += (chrVal-96)
    else:
        sum += (chrVal - 38)
print(sum)