# Problem 1             Problem2 - different problem = different solution/mindset
# ___0                  #___0___
# __000                 #__000__
# -00000                #_00000_
# 0000000               #0000000
# row=4, column =7
row=4
for i in range(0,row):
    for j in range(1, row-i):
        print('_',end="")
    for i in range(0,2*i+1):
        print('0',end='')
    print('')

#
##
###
####

####
###
##
#



# 00000
#  0000
#   000
#    00
#     0

size =5
print('')
for i in range(0, size):
    for j in range(0, size+1):
        if j== size:
            print('')
        elif j >= i:
            print('0', end='')
        else:
            print(' ', end='')

# 0
# 00
# 000
# 0000
# 00000

size =5
print('')
for i in range(0, size):
    for j in range(0, size+1):
        if j == size:
            print('')
        elif j > i:
            print(' ', end='')
        else:
            print('0', end='')

# ******
# ******
# ******
# ******
# ******
# ******
width =5
height =5
print('')
for i in range(0, height):
    for j in range(0, width):
        print('*', end='')
        if j == width-1:
            print('')


# ******
# *    *
# *    *
# *    *
# *    *
# ******


#  ****
# *    *
# ******
# *    *
# *    *



# *****
# *    *
# *****
# *    *
# *****