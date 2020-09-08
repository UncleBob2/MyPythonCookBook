import math
import subprocess
subprocess.run('reset')

end = int(input('List all prime numbers up to: '))
#end = 100
start = 3

primelist = [2]

for i in range(start, end+1):

    prime = True
    check_end = int(math.sqrt(i))
    for j in range(2, check_end+1, 1):
        if i % j == 0:
            prime = False
            break
    if prime == True:
        primelist.append(i)


print(primelist)
