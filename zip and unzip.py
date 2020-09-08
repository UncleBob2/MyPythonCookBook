import subprocess
subprocess.run('reset')

# Zip three lists
x = [1, 2, 3]
y = ['one', 'two', 'three']
z = ['I', 'II', 'III']
result = zip(x, y, z)
# Prints [(1, 'one', 'I'), (2, 'two', 'II'), (3, 'three', 'III')]

result_list = list(result)  # must use list(results)
a, b, c = zip(*result_list)  # unzip is zip(*)
print(a)
print(b)
print(c)

# common use - You can create a dictionary with list of zipped keys and values.
keys = ['name', 'age']
values = ['Bob', 25]
D = dict(zip(keys, values))
print(D)
# Prints {'age': 25, 'name': 'Bob'}

# Using zip() function you can loop through multiple lists at once.
name = ['Bob', 'Sam', 'Max']
age = [25, 35, 30]
status = ['married', 'single', 'single']
for x, y, z in zip(name, age, status):
    print(x, y, z)
# Prints Bob 25
# Prints Sam 35
# Prints Max 30
