# Really slow since the function is recursive
# def fibonacci(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for n in range(1,101):
#     print(n, ":", fibonacci(n))

# Memoization ensures that a method doesn't run for the same inputs more than
# once by keeping a record of the results for the given inputs (usually in a hash map).
# example 1 using implement explicitly, example 2 using python tool

# fibonacci_cache = {}
#
# def fibonacci(n):
#     # If we have cached the value, then return it
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#
#     #Comput the Nth term
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n > 2:
#         value = fibonacci(n-1) + fibonacci(n-2)
#
#     # Cache the value and return it
#     fibonacci_cache[n] = value
#     return value
#
# for n in range(1,101):
#     print(n,":", fibonacci(n))

from functools import lru_cache

@lru_cache(maxsize= 2000)
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,101):
    print(n, ":", fibonacci(n))