f = open('input.txt', 'r')
content = f.read().splitlines()
f.close()

def getSymbol(table, position):
    row, column = position
    if row < 0 or row >= len(table):
        return '!'
    if column < 0 or column >= len(table[0]):
        return '!'
    return table[row][column]

def getWord(table, startPosition, endPosition):
    word = ''
    startRow, startColumn = startPosition
    endRow, endColumn = endPosition
    rowMoveDirection = 1 if startRow - endRow < 0 else -1
    columnMoveDirection = 1 if startColumn - endColumn < 0 else -1
    if startRow == endRow:
        if columnMoveDirection == 1:
            while startColumn != endColumn:
                word += getSymbol(table, (startRow, startColumn))
                startColumn += 1
            return word
        if columnMoveDirection == -1:
            while startColumn != endColumn:
                word += getSymbol(table, (startRow, startColumn))
                startColumn -= 1
            return word
    if startColumn == endColumn:
        if rowMoveDirection == 1:
            while startRow != endRow:
                word += getSymbol(table, (startRow, startColumn))
                startRow += 1
            return word
        if rowMoveDirection == -1:
            while startRow != endRow:
                word += getSymbol(table, (startRow, startColumn))
                startRow -= 1
            return word
    if columnMoveDirection == 1 and rowMoveDirection == 1:
        while startRow != endRow and startColumn != endColumn:
            word += getSymbol(table, (startRow, startColumn))
            startRow += 1
            startColumn += 1
        return word
    elif columnMoveDirection == 1 and rowMoveDirection == -1:
        while startRow != endRow and startColumn != endColumn:
            word += getSymbol(table, (startRow, startColumn))
            startRow -= 1
            startColumn += 1
        return word
    elif columnMoveDirection == -1 and rowMoveDirection == 1:
        while startRow != endRow and startColumn != endColumn:
            word += getSymbol(table, (startRow, startColumn))
            startRow += 1
            startColumn -= 1
        return word
    elif columnMoveDirection == -1 and rowMoveDirection == -1:
        while startRow != endRow and startColumn != endColumn:
            word += getSymbol(table, (startRow, startColumn))
            startRow -= 1
            startColumn -= 1
        return word

def xmasCountFromPosition(table, position):
    count = 0
    row, column = position
    if table[row][column] == 'X':
        words = [
            getWord(table, (row, column), (row+4, column)),
            getWord(table, (row, column), (row-4, column)),
            getWord(table, (row, column), (row, column+4)),
            getWord(table, (row, column), (row, column-4)),
            getWord(table, (row, column), (row+4, column+4)),
            getWord(table, (row, column), (row+4, column-4)),
            getWord(table, (row, column), (row-4, column+4)),
            getWord(table, (row, column), (row-4, column-4))
        ]
        for word in words:
            if word == 'XMAS':
                count +=1
    return count
    
table = [list(line) for line in content]
sum = 0
for row in range(len(table)):
    for column in range(len(table[0])):
        sum += xmasCountFromPosition(table, (row, column))

print('sum: ' + str(sum))