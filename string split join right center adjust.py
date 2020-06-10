# Join a list of individual words into one long string.
spam = 'My name is Simon.'
print(spam)
spam = spam.split()
print('Results of spam.split(space)',spam) # Results of spam.split(space) ['My', 'name', 'is', 'Simon.']
spam = ' '.join(spam)
print("Results of ' '.join  ", spam) #Results of ' '.join   My name is Simon.
print(type(spam))
spam = spam.split('m')
print('Results of spam.split(m)',spam) # Results of spam.split(m) ['My na', 'e is Si', 'on.']
spam = 'm'.join(spam)
print("Results of ' '.join  ", spam) # Results of ' '.join   My name is Simon.

print('\nJustify right, left, and center')
print(spam.rjust(30,'='))
print(spam.ljust(30,'*'))
print(spam.center(30,'='))


def printPicnic(itemsDict, leftWidth, rightWidth):
    print()
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)  #the left column is 12 wide and right column 5 wide
printPicnic(picnicItems, 20, 6)

print()


