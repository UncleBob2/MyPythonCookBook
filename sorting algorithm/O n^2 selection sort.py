#A_list = [7, 2, 5, 4, 9, 2]
#A_list = [34, 5, 6, 81, 0, 5]
A_list = [2, 7, 4, 1, 5, 3]

# i index 0, 1, 2, 3, 4, 5 -> range does not include 5,
# len(A_list) - 1) goes up to index 3.
# the second for loop goes from i+1 to len(A_list)

'''
for i = 0 to n-1
    {
    iMin = i
    for j = i+1 to n
        {
        if A[j] < A[iMin]
        iMin = j
        }
    ###swap###
    temp = A[i]
    A[i] = A[iMin]
    A[iMin] = temp
    }
'''

print('Unsorted list', A_list)

for i in range(len(A_list) - 1):
    iMin_index = i
    for j in range(i + 1, len(A_list)):
        if A_list[j] < A_list[iMin_index]:
            iMin_index = j
    if iMin_index != i:
        A_list[i], A_list[iMin_index] = A_list[iMin_index], A_list[i]

print('Sorted list', A_list)


'''
for i in range(len(A_list) - 1):
    minIndex = i # define the lowest value via list index
    for j in range(i + 1, len(A_list)):
        if A_list[j] < A_list[minIndex]: #compare to find lowest value
            minIndex = j # lowest value is stored via indexing list instead of actual list value
    if minIndex != i:  # if
        A_list[i], A_list[minIndex] = A_list[minIndex], A_list[i] # performing the swap
print('Sorted A_list =', A_list)
'''
