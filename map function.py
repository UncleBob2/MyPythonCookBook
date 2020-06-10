# map (sequence, callback)



def main():
    listOfStr = ['hi', 'this', 'is', 'a', 'very', 'simple', 'string', 'for', 'us']
    print('*** Using map() function with lambda function ***')
    # Reverse each string in the list using lambda function & map()
    print('Original list:', listOfStr)
    modifiedList = list(map(lambda x: x[::-1], listOfStr))
    print('Modified List : ', modifiedList)

    print('\n**** Convert a string to other format using map() ****')
    sampleStr = 'this is a secret text'
    print('Original Text : ', sampleStr)
    # increment ascii value of each character by 1 in the string
    encryptedText = ''.join(map(lambda x: chr(ord(x) + 1), sampleStr))
    print('Modified Text : ', encryptedText)

    print('\n*** Passing multiple arguments to map() function ***')
    list1 = ['hi', 'this', 'is', 'a', 'very', 'simple', 'string', 'for', 'us']
    list2 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    # Join contents of two lists using map()
    modifiedList = list(map(lambda x, y: x + '_' + str(y), list1, list2))
    print('Modified List : ', modifiedList)

    print('\n*** Multiply each element in lists by a number ***')
    listOfNum = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    # Multiply each element in list by 2.
    modifiedList = list(map(lambda x, y: x * y, listOfNum, [2] * len(listOfNum)))
    print('Modified List : ', modifiedList)

    print('\n*** Using map() with dictionaries ****')

    # Transform all the values of a dictionary using map()

    dictOfNames = { 7: 'sam',  8: 'john',  9: 'mathew',   10: 'riti',    11: 'aadi',     12: 'sachin'   }

    print('Original Dictionary : ', dictOfNames)

    # add an '***' to the value field in each key value pair of dictionary
    dictOfNames = dict(map(lambda x: (x[0], x[1] + '***'), dictOfNames.items()))
    print('Modified Dictionary : ', dictOfNames)



if __name__ == '__main__':
    main()