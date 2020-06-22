# Sets in Python – do not contain duplicate values and the order does not matter
example = set()
example.add(33)
example.add(False)
example.add(3.1415)
example.add('Thorium')
print(example) # {False, 33, 3.1415}
type(example) #<class 'set'>
example.add(43)
example.add(33) # adding duplicate 33 but set will ignore it
print(example) # {False, 33, 3.1415, 43, 'Thorium'}
print(len(example))
example.discard(43) # discard is better than remove since does not give errors
example.discard(33)
print(example)

#Faster way to create set
example2 = set([28, True, 2.27928, "Helium"])
print('\n This is a second example: ', example2)
print(len(example2))
example2.clear()
print(len(example2))


# integers from 1 to 10
odds = set([1,3,5, 7,9])
evens = set([2,4,6, 8,10])
primes = set([2,3,5,7])
commposites = set([4,6,8, 9, 10])

print(odds.union(evens))
print('Odds union primes', odds.intersection(primes))
print('prime even number', primes.intersection(evens))
9 not in evens  # using "in" to provide bool answers
