# sorting a list of tuples
# sorting by two steps process with lambda

items = [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
items.sort(key=lambda x: (x[0], x[1].lower()))
print(items)
# sorting with only x[0] -> ie. only first element of tuple [(0, 'B'), (0, 'a'), (1, 'A'), (1, 'B'), (2, 'A')]
# sorting with x[0],x[1]lower() ->  [(0, 'a'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A')]
print()

# sorting a list of dictionary
# sort by name and then salary highes to lowest
employees = [{'name': 'Bill', 'salary': 100},
             {'name': 'Bill', 'salary': 76},
             {'name': 'Ted', 'salary': 67}]

# employees.sort(key=lambda x: (x['name'], x['salary'])) # this will not work, need to negate the salary to make it work
employees.sort(key=lambda x: (x['name'], -x['salary']))
print(employees)

