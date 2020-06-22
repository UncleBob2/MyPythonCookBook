# All the ins and outs of dictionaries
# immutable, once assigned can't be change in size
mydict = {'q':1, 'w':2, 't':5, 'y':6}
print('\nprint key -> value ')
for k in sorted(mydict.keys()):
    print ('key:', k, '->', mydict[k])

print('\n3. Print all the tuples in the entire dictionary ')
for tuple in mydict.items():
    print(tuple)


print('Sorting by keys and convert tuples to list')
for key in sorted(mydict.keys(), reverse= True):
    print("%s: %s" % (key, mydict[key]), end=',')

print('\nSorting by values')
for key, value in sorted(mydict.items(), key=lambda item: item[1], reverse=True):
    print("%s: %s" % (key, value), end=',')
print('\n')



print('Double Sorting: first by name then by salary')
employees = [{'name': 'Bill', 'salary': 100},
             {'name': 'Bill', 'salary': 76},
             {'name': 'Ted', 'salary': 67}]

employees.sort(key=lambda x: (x['name'], -x['salary'])) # -x need to negate the salary to make it work
print(employees)
