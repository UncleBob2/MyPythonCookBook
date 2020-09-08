# Function to determine largest element in list
def max_in_list(mylist):
    if not mylist:
        # If the length of the list is 0 then return none
        return None
    if len(mylist) == 1:
        # If the length of the list is 1 then return the
        # first element
        return mylist[0]
    else:
        # write the recursive function to return that.
        print((mylist[1:]))
        return max(mylist[0], max_in_list(mylist[1:]))


print(max_in_list([1, 2, 3, 44, 5, 9, 46, 7]))

