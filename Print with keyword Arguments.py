print('Hello')
print('World\n')

''' outputs below are:
Hello
World
'''


print('Hello', end='')
print('World \n')

''' outputs below are:
HelloWorld
'''

print('cats', 'dogs', 'mice\n')
#output
# cats dogs mice

print('cats', 'dogs', 'mice', sep=', ')
##output
# cats, dogs, mice