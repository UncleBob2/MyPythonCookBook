# Dictionary and for loop
apples = {'cox': 17, 'braeburn': 21, 'pink lady': 7, 'royal gala': 3, 'fuji': 1}
total_items = 0
for key, value in apples.items():
    total_items += value
    print(str(key), str(value))
print('total_items: ', total_items)
print()

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Sam': {'apples': 3, 'apple pies': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def total_bought(guests, items):
    num_brought = 0
    for key, value in guests.items():
        num_brought = num_brought + value.get(items, 0)
    return num_brought


print('Number of things being brought:')
print(' - Apples          ' + str(total_bought(allGuests, 'apples')))
print(' - Cups            ' + str(total_bought(allGuests, 'cups')))
print(' - Ham Sandwiches  ' + str(total_bought(allGuests, 'ham sandwiches')))

# Looping / Iterate Methods
diction = {'userid': 3203, 'message': 'hello world!', 'language': 'English'}
print('Diction loop example 1')
for key in diction.keys():
    value = diction[key]
    print(key, '=', value)

print('\nDiction loop example 2')
for key, value in diction.items():
    print(key, '=', value)

# The setdefault() method call ensures that the key is in the count dictionary (with a default value of 0)
print()
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)

print()

print()
# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        item_total += value
        print(str(value), str(key))
    print('Total number of items: ', item_total)


# displayInventory(stuff)

def addToInventory(inventory, addeditems):
    # uni_dragon_loot = {i:addeditems.count(i) for i in addeditems}
    """ Add Items to inventory
        Args:
            inventory (dict):  Inventory containing items and their counts
            addedItems (list): Items to add to inventory
        Returns:
            updatedInventory (dict): Inventory containing updated items and their counts
    """

    for i in addeditems:  # a list and looping through ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
        print('Item in list:', i, ', item in Dictionary', inventory, end='')
        inventory.setdefault(i, 0) # if no value in dic; then assign 0 else return its current value
        inventory[i] = inventory[i] + 1
        print('  , newly updated dictionary:  ', inventory)

    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
