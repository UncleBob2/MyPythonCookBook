import statistics

def main():
    # List of string
    listOfStr = ['hi', 'this', 'is', 'a', 'very', 'simple', 'string', 'for', 'us']
    print('*** Filter list using a Lambda Function ***')
    print('Original List : ', listOfStr)
    filteredList = list(filter(lambda x: len(x) == 2, listOfStr))
    print('Filtered List : ', filteredList)

    print('\n*** Filter characters from a string using filter() ***')
    strObj = 'Hi this is a sample string, a very sample string'
    filteredChars = ''.join((filter(lambda x: x not in ['a', 's'], strObj)))
    print('Filtered Characters  : ', filteredChars)

    print('\n*** Filter an array in Python using filter() ***')
    array1 = [1, 3, 4, 5, 21, 33, 45, 66, 77, 88, 99, 5, 3, 32, 55, 66, 77, 22, 3, 4, 5]
    array2 = [5, 3, 66] #filtering values
    filteredArray = list(filter(lambda x: x not in array2, array1))
    print('Filtered Array  : ', filteredArray)

    data = [1.3, 3.7, 0.8, 4.3, -0.2, 3.2]
    print('\nOriginal data set: ', data)
    avg = statistics.mean(data)
    print('the mean value: ', round(statistics.mean(data),3))
    above_avg = list(filter(lambda x:x>avg,data))
    print('all values above the mean: ', above_avg)

    #remove missing data
    countries =['', 'Argentina', '', 'Brazil', 'Chile', '', 'Venezuela']
    print('\nraw list of countries', countries)
    cleanlist = list(filter(None,countries))
    print('Filtered Countries',cleanlist  )

if __name__ == '__main__':
    main()