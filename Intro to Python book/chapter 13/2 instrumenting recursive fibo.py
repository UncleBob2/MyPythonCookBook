from __future__ import print_function

# This Calculates the Fibonacci number Along with the number
# of calls being made


class Fibonacci:
    def __init__(self):
        # Set the count to zero whenever an object is
        # initialized
        self.count = 0

    def fib(self, num):
        # This is the main part of the function
        # Calculating the base cases
        if num == 0 or num == 1:
            return num
        else:
            # solving recursively
            answer = self.fib(num - 1) + self.fib(num - 2)
            # incrementing the count by 2 as two calls are being made
            self.count += 2
            # return the final answer
            return answer

    def getCount(self):
        # GEt the count value
        return self.count

    def resetCount(self):
        # Resetting the value of the count
        self.count = 0
        # Define main function


def main():
    # Create an object of Fibonacci class and then call different method of it.
    some_object = Fibonacci()
    # calling fib() function
    print("The answer is :", some_object.fib(5))
    # calling getCount() function
    print("The count is :", some_object.getCount())
    print("Count is reset to zero")
    # calling resetCount() function
    some_object.resetCount()
    print("The count is :", some_object.getCount())
    # Calling the main function


if __name__ == "__main__":
    main()
