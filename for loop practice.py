# _____o
# ____ooo
# ___ooooo
# __ooooooo
# _ooooooooo


for row in range(0,5):
    for column in range(1,5-row):
        print(' ',end='')
    for pyramid in range(0,2*row+1):
        print('o',end='')
    print()


# # # #
# # # #
# # # #
# # # #
print()

for row in range (0,4):
    for column in range (0,4):
        print('# ',end='')
    print()

# # # #
# # #
# #
#
print()

for row in range(0,4):
    for column in range(0,4-row):
        print('# ',end='')
    print()


#
# #
# # #
# # # #
print()

for i in range(0,4):
    for j in range(0,i+1):
        print('# ',end='')
    print()


print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(0,6):
    for j in range(0,9):
        print(grid[j][i],end='')

    print()





