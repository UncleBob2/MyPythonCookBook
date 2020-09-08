import math
import subprocess
subprocess.run('reset')


def isPrime(n):
    upto = int(math.sqrt(n))
    for i in range(2, upto+1):
        if n % i == 0:
            return False
    return True


def goldbach(num):
    if num % 2 == 1:
        print("Please enter even number only")
        return
    start = 2
    pair_prime = num - start
    while(num > start):
        #print(start, pair_prime)
        if isPrime(start) and isPrime(pair_prime):
            print(start, '\t', pair_prime)
            return
        start += 1
        pair_prime = num - start


goldbach(8)
