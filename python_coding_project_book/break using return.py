
import math



def is_prime(n):
    # get the square root
    nsqrt = int(math.sqrt(n))
    # 1Terate through the range
    for i in range(2, nsqrt + 1):
        if n % i == 0:
            return False
    return True


def Goldman(user_num):
    if user_num % 2 == 0:
        pass

    start = 3
    another = user_num - start
    while start < user_num:
        if is_prime(start) and is_prime(another):
            print(start, "\t", another)
            return# will escape out of both if and while loop
        start += 2
        another = user_num - start
        print(start, user_num, another)


print("The Goldman two primes are: ")

Goldman(4)