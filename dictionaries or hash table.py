# All the ins and outs of dictionaries
# immutable, once assigned can't be change in size

print('\n1. See code for declaring dictionary && assigning individual elements')
d = { }  # declare dictionary && assigning individual elements
d['a'] = 'alpha' #key = a, storage alpha at key a
d['o'] = 'omega'
print('2. Printing items, keys, and values of a dictionary')
print(d.items()) #print(d.keys()) print(d.values())
print(d['a'])
print(d.get('o')) # using get to avoid none existing index
print('Is a in d?' , 'a' in d)


print('\nprint key -> value ')
for k in sorted(d.keys()):
    print ('key:', k, '->', d[k])

print('\n3. Print all the tuples in the entire dictionary ')
for tuple in d.items():
    print(tuple)

mydict = {'q':1, 'w':2, 't':5, 'y':6}
print('\n4. Simple sort of dictionary into type list',sorted(mydict) )


print('Sorting by keys')
for key in sorted(mydict.keys()):
    print("%s: %s" % (key, mydict[key]), end=',')

print('\nSorting by values')
for key, value in sorted(mydict.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value), end=',')
print('\n')


line = 'Converting a text string to list and then converting to dictionary'
print(line)
frequency= { }
txt = line.lower().split()
for item in txt:  # assigning dictionary key and values
    frequency[item] = txt.count(item)
print(frequency.items())
print()

print('Sorting twice: first by name then by salary')
employees = [{'name': 'Bill', 'salary': 100},
             {'name': 'Bill', 'salary': 76},
             {'name': 'Ted', 'salary': 67}]

# employees.sort(key=lambda x: (x['name'], x['salary'])) # this will not work, need to negate the salary to make it work
employees.sort(key=lambda x: (x['name'], -x['salary']))
print(employees)
