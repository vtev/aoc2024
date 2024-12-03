import re

f = open('input.txt', 'r')
content = f.read().splitlines()
f.close()

sum = 0
for line in content:
    result = re.findall(r'mul\((\d{1,3},\d{1,3})\)', line)
    for mul in result:
        firstNum, secondNum = mul.split(',')
        sum += int(firstNum) * int(secondNum)

print(sum)