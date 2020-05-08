def main():
    # Create a tuple from list by type casting
    tupleObj = (12, 34, 45, 22, 33)
    print("****** Append an element in Tuple at end ******")
    print("Original Tuple : ", tupleObj)
    # Append 19 at the end of tuple
    tupleObj = tupleObj + (19,)
    print("Modified Tuple : ", tupleObj)

    print("\n******* Insert an element at specific index in tuple *******")
    print("Original Tuple : ", tupleObj)
    n = 2
    # Insert 19 in tuple at index 2
    tupleObj = tupleObj[: n] + (19,) + tupleObj[n:]
    print("Modified Tuple : ", tupleObj)

    print("\n******* Modify / Replace the element at specific index in tuple *******")
    print("Original Tuple : ", tupleObj)
    n = 2
    # Replace the element at index 2 to 'Test'
    tupleObj = tupleObj[: n] + ('test',) + tupleObj[n + 1:]
    print("Modified Tuple : ", tupleObj)

    print("\n******* Delete the element at specific index in tuple *******")
    print("Original Tuple : ", tupleObj)
    n = 2
    # Delete the element at index 2
    tupleObj = tupleObj[: n] + tupleObj[n + 1:]
    print("Modified Tuple : ", tupleObj)


if __name__ == '__main__':
    main()

#thispointer.com