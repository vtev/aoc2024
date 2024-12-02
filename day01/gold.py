f = open('input.txt', 'r')
content = f.read().splitlines()
f.close()
values = []
count = {}
for line in content:
    first, second = line.split('   ')
    values.append(first)
    if count.get(second) != None:
        count[second] = count[second] + 1
    else:
        count[second] = 1
sum = 0
for value in values:
    sum += int(value) * count.get(value, 0)

print(sum)