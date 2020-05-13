# List [] vs Tuple () vs Dictionary vs Set{}

# List [] – add, remove, and change data             ['apple', 'banana', 'cherry']
# Tuple () – once created, cannot change in size or content i.e. immutable  i.e. coordinate(x,y,z)      ('apple', 'banana', 'cherry')
# Set {}  - is unordered and has no duplicate values             {'apple', 'banana', 'cherry'}
# Dictionary{:} keys, not ordered data(aka array,map) {'name':'apple, 'color':'green'}

# Below is an example of a list with square brackets
earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
earth_metals.sort()
print(earth_metals)

for i in earth_metals:
    print(i)

print('\nMixed list examples of int, float, string, bool ')
spam = [444, 3.1415,'hello', True, None, 42]

for i in spam:
    print(i)

# Below is an example of a tuple with round brackets
earth_metals = ('Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium')
print('\nExample of tuple ', earth_metals)

try:
    earth_metals.sort()
except AttributeError:
    print('Error: can not sort immutable tuple.\n')


example = set()
example.add(33)
example.add(False)
example.add(3.1415)
print('Set example',example, type(example))


example.remove or example.discard
example2 = set([28, True, 2.27928, "Helium"])
print(example2, type(example2))

diction = {'userid': 3203, 'message': 'hello world!', 'language': 'English'}
print('\nDictionary example', diction)
#Method 1:
if 'location' in diction:
    print(diction['location'])
else:
   print('Diction does not contain a location value.')

# Method 2:
# Try:
#        Print(diction['location']
# Except KeyError:
#    print('Diction does not contain a location value.')

# Method 3:
Loc = diction.get('message', None)
print('example3 ',Loc)

Loc = diction.get(None, 'English')
print('example4 ',Loc +'\n')
#
