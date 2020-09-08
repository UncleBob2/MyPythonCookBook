"""Computer scientists and mathematicians often use numbering systems other than base 10. Write a program that allows a user to enter a number and a base and then prints out the digits of the number in the new base. Use a recursive function baseConversion(num,base) to print the digits.
Hint: Consider base 10. To get the rightmost digit of a base 10 number, simply look at the remainder after dividing by 10. For example, 153%10 is 3. To get the remaining digits, you repeat the process on 15, which is just 153/10. This same process works for any base. The only problem is that we get the digits in reverse order (right to left).
Write a recursive function that first prints the digits of num//base and then prints the last digit, namely num%base. You should put a space between successive digits, since bases greater than 10 will print out with multi-character digits. For example, baseConversion(245, 16) should print 15 5."""

# define a function to convert decimal number into base 16
def baseConversion(num, base, mylist):
    # The items in the list represent the representation
    # in that base#set the base caseUse if-else statement to check num is equal to 0 or not.
    if num == 0:
        # reverse element of list
        mylist.reverse()
        print(mylist)
    else:
        # As suggested reverse the list
        mylist.append(num % base)
        # change the num now
        num = int(num / base)
        # recursively call the same function
        baseConversion(num, base, mylist)


print("245 in base 16 is: ")
# call function to determine 245 in base 16
baseConversion(245, 16, [])

