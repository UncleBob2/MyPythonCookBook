mylist = [
    "Zero",
    "One",
    "Two",
    "Three",
    # list is defined as per conditions
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine"]


# method inEnglish is defined to convert int to words
def inEnglish(num):
    # declared mylist as global for making it constant without any error
    global mylist
    # if num is 0, without any further delay we are returning string Zero to the main
    if(num == 0):
        return "Zero"
    # initialization of string to store words
    mystring = ""
    while(num > 0):                                                   # looping to get every value
        # getting last value of the num
        rem = num % 10
        # checking condition to add releavant word to the mystring
        if(num//10):
            # space is added to the string for clear output
            mystring = inEnglish(int(num/10))+" "+mylist[rem]
        else:                                                       # if, if fails then else block will add the
            mystring = mylist[rem]+" "+mystring
        # returning the string to the main
        return mystring


print("678 in words are: ")
print(inEnglish(999))
