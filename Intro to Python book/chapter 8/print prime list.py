import os
import math
import subprocess
subprocess.run('reset')


def isprime(n):
    start = 2
    end = int(math.sqrt(n))+1
    for i in range(start, end):
        #print('check indexing', start, end)
        if n % i == 0:
            #print(n, i)
            return False
            # break
        # want to complete checking all the numbers from start to end. It can only a prime number to exit the loop
    return True


def primelist(number):
    numbers = number
    for i in range(2, numbers+1):
        if isprime(i) == True:
            print(i, end=", ")


primelist(500)
