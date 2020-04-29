# List [] vs Tuple ()
# List – add, remove, and change data
# Tuple – cannot be changed i.e. immutable

# Below is an example of a list with square brackets
earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
earth_metals.sort()
print(earth_metals)

for i in earth_metals:
    print(i)


# ['Barium', 'Beryllium', 'Calcium', 'Magnesium', 'Radium', 'Strontium']

spam = [444, 3.1415,'hello', True, None, 42]
#spam = [444, 3.1415,7,88, 99, 42]

for i in spam:
    print(i)

# Below is an example of a tuple with round brackets
earth_metals = ('Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium')
print(earth_metals)

for i in earth_metals:
    print(i)

#earth_metals.sort()


'''
Traceback (most recent call last):
  File
 "<pyshell#147>", line 1, in <module>
    earth_metals.sort()
AttributeError: 'tuple' object has no attribute 'sort'
'''
