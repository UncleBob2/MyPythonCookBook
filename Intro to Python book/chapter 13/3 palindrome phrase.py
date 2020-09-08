import string

# Define function to read string from user
def main():
    # read input from user
    inp = input("Enter a string: ")

    # call check_palindrome() function to check user entered
    # string is a palindrome or not.
    result = check_palindrome(inp)

    # Use if-else statement to display message according to return value of check_palindrome()
    # function.

    if result == True:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")


def check_palindrome(mystring):
    # remove all punctuations from user entered string
    mystring = "".join(
        [chars.lower() for chars in mystring if chars not in string.punctuation]
    )

    # remove space from user entered string
    mystring = mystring.replace(" ", "")

    # Use if-else statement to return true if whole string is traversed otherwise false.
    if len(mystring) == 0 or len(mystring) == 1:
        # return call to calling function
        return True
    else:
        # again call check_palindrome() function.
        return mystring[0] == mystring[-1] and (check_palindrome(mystring[1:-1]))


if __name__ == "__main__":
    main()
