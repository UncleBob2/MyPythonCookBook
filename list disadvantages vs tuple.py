# List [] vs Tuple ()
# # List – add, remove, and change data
# # Tuple – cannot be  changed, immutable, can be generate more quickly
# primeNumbers = [2,3,5,7,11,13, 17]
# lists have more methods, consume more memory, take more time: append, clear, copy, count, extend, index, pop, reverse, sort
import timeit
import sys
list_eg = [1,2,3,'a','b','c', True, 3.14159]
tuple_eg = (1,2,3,'a','b', 'c', True, 3.14159)

#tuple with one element behaves accentrically, must place a comma based on tuple assignment

# tuple quick assignment

print('List size = ', sys.getsizeof(list_eg))   # List size = 120
print('Tuple size = ', sys.getsizeof(tuple_eg)) # Tuple size = 104, tuple is smaller and better than list

list_create = timeit.timeit(stmt='[1,2,3,4,5,6,7,9,10]', number=100000000)
print('List create in sec: ', list_create)

tuple_create = timeit.timeit(stmt='(1,2,3,4,5,6,7,9,10)', number=100000000)
print('List create in sec: ', tuple_create)




