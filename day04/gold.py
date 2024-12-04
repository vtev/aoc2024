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
    row, column = position
    if table[row][column] == 'A':
        if ((getWord(table, (row+1, column-1), (row-2, column+2)) == 'MAS'
                or getWord(table, (row-1, column+1), (row+2, column-2)) == 'MAS')
            and (getWord(table, (row+1, column+1), (row-2, column-2)) == 'MAS'
                 or getWord(table, (row-1, column-1), (row+2, column+2)) == 'MAS')):
            return 1
    return 0
    
table = [list(line) for line in content]
sum = 0
for row in range(len(table)):
    for column in range(len(table[0])):
        sum += xmasCountFromPosition(table, (row, column))

print('sum: ' + str(sum))