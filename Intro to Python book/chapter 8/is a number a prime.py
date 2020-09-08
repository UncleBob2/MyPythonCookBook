import math
import subprocess
subprocess.run('reset')

number = int(input('Please enter a number: '))
start = 2
end = int(math.sqrt(number))
prime = True

for i in range(start, end, 1):
    if number % i == 0:
        prime = False
        print('This is NOT a prime number: ', number)
        break

if prime == True:
    print('PRIME NUMBER:', number)
