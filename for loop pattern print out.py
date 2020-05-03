
print()
#  *****
# *     *
# *     *
# *******
# *     *
# *     *

for i in range(6):
    for j in range(6):
        if ((j ==0 or j==5 or i==3 or i==0) and not ((i==0 and j==0) or(i==0 and j==5)) ):
            print('*',end='')
        else:
            print(' ',end='')
    print()


# ****
# *   *
# *   *
# ****
# *   *
# *   *
# *****
print()

for row in range(7):
    for col in range(5):
        if((row ==0 or row==3 or row==6 or col ==0 ) and not col==4) or (col ==4 and (row==1 or row==2 or row==4 or row==5)) :
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

# *****
# *
# *
# *
# *
# *
# *****

for row in range(7):
    for col in range(5):
        if (row==0 or row ==6 or col ==0) and not(col==0 and (row==0 or row==6)):
            print('*',end='')
        else:
            print(' ',end='')
    print()

print()

# *     *
# **   **
# * * * *
# *  *  *
# *     *
# *     *
# *     *

for row in range(7):
    for col in range(7):
        if (col == 0 or col ==6) or (row==1 and (col ==1 or col ==5)) or (row==2 and (col==2 or col==4)) or (row==3 and col ==3):
            print('*',end='')
        else:
            print(' ',end='')
    print()



print()

# *   *
# *  *
# * *
# **
# *  *
# *   *
# *    *

for row in range(7):
    for col in range(5):
        if (col ==0) or (row + col ==4) or (row - col ==2):
            print('*',end='')
        else:
            print(' ',end='')
    print()

