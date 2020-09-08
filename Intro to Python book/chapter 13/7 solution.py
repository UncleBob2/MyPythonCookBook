def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        answer = 1
        # Use while loop to which continue iterate till value of nis greater than 1.
        while n != 1:
            answer *= n
            n -= 1
        return answer


# Define function to determine combination using iterative
# approach


def combinations(n, k):
    print("Iterative Approach:")
    print("The combinations(5,2) is:")
    print(fact(n) / (fact(k) * fact(n - k)))


combinations(50, 5)

