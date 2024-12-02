f = open('input.txt', 'r')
content = f.read().splitlines()
f.close()

def getSign(num):
    return 'negative' if num < 0 else 'positive'

def isReportSafe(report):
    values = report.split(' ')
    sign = ''
    for i in range(len(values) - 1):
       step = int(values[i]) - int(values[i + 1])
       if abs(step) < 1 or abs(step) > 3:
           return False
       if i == 0:
          sign = getSign(step)
       elif sign != getSign(step):
          return False
    return True

numberOfSafeReports = 0
for line in content:
    if (isReportSafe(line)): numberOfSafeReports += 1

print(numberOfSafeReports)