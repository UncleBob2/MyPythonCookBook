def main():
    # A tuple of numbers
    tupleObj = (12, 34, 45, 22, 33, 67, 34, 56)

    print("**** Find an element in tuple using 'in' & 'not in' *****")

    # Check if element 34 exists in tuple
    if 34 in tupleObj:
        print("Element Found in Tuple")
    else:
        print("Element not Found in Tuple")
        # Check if element 1001 doesn't exists in tuple
    if 1001 not in tupleObj:
        print("Yes, element NOT In tuple")
    else:
        print("Element is in Tuple")

    print("\n**** Find the index of an element in Tuple *****")

    # Find the index of 24 in tuple, if not found then handle the exception
    try:
        pos = tupleObj.index(24)
        print("Element 24 Found at : ", pos)
    except ValueError as e:
        print(e)

    # Find the index of 34 in tuple, if not found then handle the exception
    try:
        pos = tupleObj.index(34)
        print("Element 34 Found at : ", pos)
    except ValueError as e:
        print(e)

    print("\n**** Find the occurence count an element in the Tuple *****")

    # Get the count of how many times 34 appears in tuple
    count = tupleObj.count(34)

    print("Occurance count of 34 in tuple is : ", count)

    # Based on occurrence count check if element exists in tuple
    if tupleObj.count(34) > 0:
        print("element 34 Found in Tuple")
    else:
        print("element 34 Not Found in Tuple")


if __name__ == '__main__':
    main()