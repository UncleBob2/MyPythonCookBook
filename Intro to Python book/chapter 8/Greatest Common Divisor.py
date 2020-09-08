'''
The greatest common divisor (GCD) of two values can be computed using Euclid’s algorithm. Starting with the values m and n, we repeatedly apply the swapping formula: (n, m) = (m, n%m) until m is 0. At that point, n is the GCD of the original m and n. Write a program that finds the GCD of two numbers using this algorithm.
'''


def gcd(n, m):
    while(m != 0):
        # Swap as instructed
        n, m = m, n % m
        print(n, m, 'n%m')
    return(n)


print("The gcd of 2 and 5 is:", gcd(2, 5))

print("The gcd of 8 and 13 is:", gcd(8, 13))

print("The gcd of 100 and 143 is:", gcd(100, 120))
