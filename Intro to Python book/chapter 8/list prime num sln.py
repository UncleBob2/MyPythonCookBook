import math


def is_prime(n):
    '''Define the function to check whether number is prime or not'''
    nsqrt = int(math.sqrt(n))
    # Use the for loop to iterate. Iterate through the square root of the number
    # #|Terate through the range
    for i in range(2, nsqrt+1):
        if(n % i == 0):
            # If it divides then print and return
            return(False)
    # If it is not divided by any return true
    return(True)


def printPrimesTo(num):
    # Use proper delimiters in the print statement
    print('Printing all the prime numbers below', num)
    for i in range(3, num+1):
        if(is_prime(i)):
            print(i, end=" \t")
    print("\n")


printPrimesTo(5)
printPrimesTo(101)
printPrimesTo(50)
