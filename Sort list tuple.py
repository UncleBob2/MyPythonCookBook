# Can't directly sort tuple because tuple is immutable object use "sorted"

# Example sort by planets' size
planets =[
    #name, radius(km), density(g/cm^3), distance from the sun(Astro unit)
    ('Mercury', 2440, 5.43, 0.396),
    ('Venus', 6052, 5.24, 0.723),
    ('Earth', 6378, 5.52, 1.00),
    ('Mars', 3396, 3.93, 1.530)]
print('Original list of planets', planets)
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print('Planets sort by radius:', planets)

# Example sort by planets's density
density = lambda planet: planet[2]
planets.sort(key=density)
print('Planets sort by density:', planets)
print()

# Use sorted() to sort a tuple and create a sorted copy
data = (7,2,5,6,1,3,9,10)
print('Original tuple:', data)
print('Tuple become a list with sorted:', sorted(data)) # the original tuple is not alter

print(sorted('Alphabetical'))

print()

# sort(...)
# L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
# reverse = False => sort in ascending order
# reverse = True => sort in descending order
# *IN PLACE* does not create a 2nd data structure;hence, would change the existing data
# key = <sorting function>

# Below is an example of a list with square brackets
earth_metals = ['Beryllium', 'Magnesium', 'Calcium', 'Strontium', 'Barium', 'Radium']
earth_metals.sort()
print(earth_metals)
earth_metals.sort(reverse=True)
print(earth_metals)
