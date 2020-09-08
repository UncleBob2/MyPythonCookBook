count = 0


def fib(num):
    # Use the Fibonacci formula
    # But before that implement all the base cases
    # Commenting ...
    print("Computing fib(%d)" % (num))
    # Use if-else statement to determine whether last element of Fibonacci series reached or not.
    if num == 0 or num == 1:
        print("Leaving fib(%d) and returning %d" % (num, num))
        return num
    else:
        # check value of num is 3 or not
        if num == 3:
            global count
            count += 1

    # recursively calling the main function
    answer = fib(num - 1) + fib(num - 2)
    print("Leaving fib(%d) and returning %d" % (num, answer))
    return answer


# Display Fibonacci of 10 and number of times fib(3) is called.
print("The value of fib of 10 :", fib(10))
print("The number of times fib(3) is called is :", count)

