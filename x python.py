
def printTable(items, col_width ):
    # print('Left width: ' + str(col_width[0]) + ' Center width: ' + str(col_width[1]) + ' Right width: ' + str(col_width[2]))
    rows = len(items[0])
    colums = len(items)
    print(rows, colums)
    for row in range(rows):
        #print(items[0][row].rjust(col_width[0]) + ' ' + items[1][row].rjust(col_width[1]) + ' ' + items[2][row].rjust(col_width[2]))
        for col in range(colums):
            print(items[col][row].rjust(col_width[col]) + ' ',end="")
        print()

    # print(items[0][0].rjust(col_width[0]) + ' ' + items[1][0].rjust(col_width[1]) + ' ' + items[2][0].rjust(col_width[2]))
    # print(items[0][1].rjust(col_width[0]) + ' ' + items[1][1].rjust(col_width[1]) + ' ' + items[2][1].rjust(col_width[2]))
    # print(items[0][2].rjust(col_width[0]) + ' ' + items[1][2].rjust(col_width[1]) + ' ' + items[2][2].rjust(col_width[2]))
    # print(items[0][3].rjust(col_width[0]) + ' ' + items[1][3].rjust(col_width[1]) + ' ' + items[2][3].rjust(col_width[2]))





tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

#printTable(tableData)
col_width = [0] * len(tableData)

for i in range(len(tableData)):
    # print(tableData[i])
    # print(max(tableData[i],key=len))
    col_width[i] = len(max(tableData[i],key=len))

#print(col_width)

printTable(tableData,col_width)
