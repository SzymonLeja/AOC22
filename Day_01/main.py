inputFile = open("input.txt", "r")
elfCounter = 0
elfArray = [0] * 99999
for line in inputFile:
    if line in ('\n', '\r\n'):
        elfCounter+=1
    else:
        elfArray[elfCounter] += int(line)
print(max(elfArray))