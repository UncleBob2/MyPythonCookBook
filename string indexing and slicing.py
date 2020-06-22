# Python strings cannot be changed — they are immutable.
# If you need a different string, you should create a new one:

word ='python'
print('The character in position 0', word[0])
print('The character in position 5', word[5])
# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
print('The last character', word[-1])
print('The third last character', word[-4])
print()

print("The sum of 1 + 2 is {0}".format(1+2)) # str.format(*args, **kwargs)
print('slicing example 1 backward:', word[2:]+word[:2])
print('slicing example 2 correct:', word[:2]+word[2:])


spam = "python"
print('# Iterate over the string without indexing')
for value in spam:
   print(value, end='..')


print()

print('\n # Iterate over the string using indexing')
for value in range(0,len(spam)):
    print(spam[value], end='')

print()

print('\n # Iterate over the string using enumerate type')
for value,char in enumerate(spam):
    print(char, end='')
print('\n\n')



for i in range(6):
    for value in range(i+1):
        print(spam[value], end='')
    print()

#
# p
# py
# pyt
# pyth
# pytho
# python