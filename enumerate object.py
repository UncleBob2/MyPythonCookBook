names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names, 1):
    print(f'{index}: {value}')

 '''
# HARMFUL: Don't do this
for i in range(len(my_items)):
    print(i, my_items[i])
 '''


# Create a list that can be enumerated
L = ['red', 'green', 'blue']
x = list(enumerate(L))
print(x)
# Prints [(0, 'red'), (1, 'green'), (2, 'blue')]


# Start counter from 10
L = ['red', 'green', 'blue']
x = list(enumerate(L, 10))
print(x)
# Prints [(10, 'red'), (11, 'green'), (12, 'blue')]

# When you iterate an enumerate object, you get a tuple containing (counter, item)

L = ['red', 'green', 'blue']
for pair in enumerate(L):
    print(pair)
# Prints (0, 'red')
# Prints (1, 'green')
# Prints (2, 'blue')

# You can unpack the tuple into multiple variables as well.
L = ['red', 'green', 'blue']
for index, item in enumerate(L):
    print(index, item)
# Prints 0 red
# Prints 1 green
# Prints 2 blue
