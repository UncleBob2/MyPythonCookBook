# Object ID, check if the two objects have the same object in memory

a = [1,2,3]
b = [1,2,3]

print('print true if a and b are equal =', a==b)

print('print true if a and b same object =', a is b)

print(id(a) == id(b))

print(id(a))
print(id(b))

b = a
print(id(a))
print(id(b))


