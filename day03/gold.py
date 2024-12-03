import re

f = open('input.txt', 'r')
content = f.read().splitlines()
f.close()

sum = 0
count = True
for line in content:
    result = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
    for cell in result:
        if cell == "don't()":
            count = False
        elif cell == "do()":
            count = True
        elif count:
            match = re.search(r'(\d{1,3}),(\d{1,3})', cell)
            sum += int(match.group(1)) * int(match.group(2))

print(sum)