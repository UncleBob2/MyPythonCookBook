# List [] vs Tuple () vs Dictionary vs Set{}

# List [] – add, remove, and change data             ['apple', 'banana', 'cherry']
# Tuple () – cannot be changed i.e. immutable        ('apple', 'banana', 'cherry')
# Set {}  - ordered, no duplicate values             {'apple', 'banana', 'cherry'}
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

#Looping / Iterate Methods
diction = {'userid': 3203, 'message': 'hello world!', 'language': 'English'}
print('Diction loop example 1')
for key in diction.keys():
   value = diction[key]
   print(key, '=', value)

print('\nDiction loop example 2')
for key, value in diction.items():
    print(key, '=', value)

#The setdefault() method call ensures that the key is in the count dictionary (with a default value of 0)
print()
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)

print()

allGuests = {'Alice': {'apples':5, 'pretzels':12},
             'Bob': {'ham sandwiches':3, 'apples':2},
             'Carol': {'cups':3, 'apple pies':1}}

def total_bought(guests,items):
    num_brought = 0
    for key,value in guests.items():
        num_brought= num_brought + value.get(items,0)
    return num_brought

print('Number of things being brought:')
print(' - Apples          '+ str(total_bought(allGuests,'apples')))
print(' - Cups            '+ str(total_bought(allGuests, 'cups')))
print(' - Ham Sandwiches  '+ str(total_bought(allGuests, 'ham sandwiches')) )



print()
# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total +v.get(inventory)
    print("Total number of items: " + str(item_total))


displayInventory(stuff)