names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# zip is a iterator and for efficiency, it can only loop through one time
identities = list(zip(names, heroes))

print(identities)

for identity in identities:
    print('{} is actually {}!'.format(identity[0], identity[1]))
