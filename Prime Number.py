import time, math
import textwrap
def is_prime(n):
    '''Return "True" if "n" is a prime number. False otherwise. '''

    if n ==1:
        return False # 1 is not a prime number
    #If it's even and not 2, then it's not prime
    if n ==2:
        return True
    if n > 2 and n%2==0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, max_divisor,2):
        if n%d == 0:
            return False
            break
    return True




#========Test Function ===========
t0 = time.time()
prime_list = []
upper = 100_000;


for n in range(1, upper):
    prime = is_prime(n)
    if prime == True:
        prime_list.append(n)
t1 = time.time()
print("Time required: ", t1 -t0)

#convert a list of integer to string
prime_list = ''.join(str(prime_list))

wrapper = textwrap.TextWrapper(width=150)
word_list = wrapper.wrap(text= prime_list)

for element in word_list:
    print(element)



