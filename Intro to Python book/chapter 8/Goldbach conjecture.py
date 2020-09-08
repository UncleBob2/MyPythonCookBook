import os
import math
import subprocess

subprocess.run("reset")

plist = []


def isprime(num):
    start = 2
    stop = int(math.sqrt(num)) + 1
    for i in range(start, stop):
        if num % i == 0:
            return False
    return True


def primelist(stop):
    for i in range(2, stop + 1):
        if isprime(i) == True:
            plist.append(i)


def gold(n):
    if n % 2 != 0:
        print("Please enter even number: ")
    else:
        primelist(n)
        # print(plist)


def two_primes(x, plist):
    sum = 0
    while sum != x:
        for i in range(len(plist)):
            pair_num = x - plist[i]
            sum = pair_num + plist[i]
            if sum == x and (pair_num in plist):
                sum = pair_num + plist[i]
                print(pair_num, plist[i])
                break


x = 150
gold(x)
two_primes(x, plist)
