items = [(1,'B'), (1,'A'), (2, 'A'), (0,'B'), (0,'a')]
items.sort(key=lambda x: (x[0], x[1].lower()))
print(items)
# sorting with only x[0] -> ie. only first element of tuple [(0, 'B'), (0, 'a'), (1, 'A'), (1, 'B'), (2, 'A')]
# sorting with x[0],x[1]lower() ->  [(0, 'a'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A')]
print()

# Example sort by planets' size
planets =[
    #name, radius(km), density(g/cm^3), distance from the sun(Astro unit)
    ('A', 2440, 5.43, 0.396),
    ('c', 6052, 5.24, 0.723),
    ('B', 6378, 5.52, 1.00),
    ('a', 3396, 3.93, 1.530)]

# Example sort by planets's density
density = lambda planet: planet[2]
planets.sort(key=density)
print('Planets sort by density:', planets)
print() # Planets sort by density: [('a', 3396, 3.93, 1.53), ('c', 6052, 5.24, 0.723), ('A', 2440, 5.43, 0.396), ('B', 6378, 5.52, 1.0)]
lowercase = lambda planet: planet[0].lower()
planets.sort(key=lowercase)
print('second sort', planets)