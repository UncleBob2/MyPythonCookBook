# Duck tests - walk like a duck, quack like a duck - it must be a duck (sometime wrong but most time ok)
# Duck tests - we don't care if it is a duck or not. We just want it to behave like a duck.
# Easier to ask forgiveness than permission (EAFP) - not advised to check all the times for attritutes

#person = {'name': 'Jess', 'age': 23, 'job': 'programmer'}
person = {'name': 'Jess', 'age': 23}
# LBYL - non pythonic
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))

else:
    print('Missing some keys')

# EAFP (Pythonic - no check at all (if))
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))


my_list = [1, 2, 3, 4, 5, 6]

# Non-Pythonic
if len(my_list) > 6: # asking permissions/tests require to access object several times
    print(my_list[6])
else:
    print('That index does not exist')

# Pythonic
try:
    print(my_list[6])
except IndexError: # access object once, more readable
    print('That index does not exist')
