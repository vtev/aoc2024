f = open('input.txt', 'r')
content = f.read().splitlines()
f.close()
firstList = []
secondList = []
for line in content:
    first, second = line.split('   ')
    firstList.append(first)
    secondList.append(second)
sum = 0
while len(firstList) != 0:
    minFirstList = min(firstList)
    minSecondList = min(secondList)
    sum += abs(int(minFirstList) - int(minSecondList))
    firstList.remove(minFirstList)
    secondList.remove(minSecondList)

print(sum)