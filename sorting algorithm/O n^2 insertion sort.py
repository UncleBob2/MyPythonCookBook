
A_list = [7, 2, 5, 4, 9, 2]
#A_list = [34, 5, 6, 81, 0, 5]
#A_list = [2, 7, 4, 1, 5, 3]

# draw a line and create a sorted and unsorted sets, pick one card at a time and move to sorted set
# pick up a card in the unsorted set into the sorted set
# start shifting and inserting
'''
for i = 1 to n-1    #len(A_list) = n-1 since range does not include the last value
{
    value = A[i]
    hole = i
    while(hole > 0 && A[hole -1] > value)
    {
    A[hole] = A[hole -1]
    hole = hole -1
    }
    A[hole] = value
}
'''
print('Unsorted array', A_list)
for i in range(1, len(A_list)):
    value = A_list[i]
    hole = i
    while(hole > 0 and A_list[hole - 1] > value):
        A_list[hole] = A_list[hole - 1]
        hole = hole - 1
    A_list[hole] = value
print('Sorted array', A_list)


'''
for index in range(1, len(A_list)):
    current_element = A_list[index]
    pos = index
    while current_element < A_list[pos - 1] and pos > 0:
        A_list[pos] = A_list[pos - 1]
        pos = pos - 1
    A_list[pos] = current_element

print(A_list)'''

# A) Insertion sort vs. Selection sort
# insertion sort take the element immediately following the sorted data, scan through the sorted data to find a place to put it within the sorted data

# Selection sort - scan through the unsorted data looking for the smallest remaining element , the swap it into the position immediately following the sorted data. repeat.
