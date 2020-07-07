# Lists – preserve index orders, index[-1], slicing[2:6] – use Bracket [   ]
primes =[2,3,5,7,11,13]
primes.append(17)
primes.append(19)
print(primes)
print(primes[3]) # index
print(primes[2:5]) # slicing - first value include but not last value
print(primes[2:]) # slicing
print(primes[-1]) #last number


# list of different element types
example = [128, True, "alpha", 1.7343, [65,False]]
numbers = [1,2,3]
letters = ['a','b','c']
print(numbers+letters) # concatenation

