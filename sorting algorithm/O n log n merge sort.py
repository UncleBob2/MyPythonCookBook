#data = [7, 2, 5, 66, 3, 4, 9, 2]
data = [1, 2, 6, 32, 6, 643, 343, 245, 789, 32, 654]
#data = [10, 15, 4, 23, 88, 1, 2, 4]
#data = [10, 15, 4, 23, 1, 2, 4]
# recursive, O(len_left_halfogn)

# Python program for implementation of MergeSort
'''
1) divide and conquer
2) recursive
3) stable - equal keys = relative order same as the original list (1,2), (2,5), (4,8), (2,3) => (1,2), (2,5), (2,3), (4,8)
4) not In-Place - extra memory is required

merge_sort(data)
{
    n = length(data)
    if (n < 2) return # based/exit condition
    middle = n //2
    left_half = array of size (middle)
    right_half = array of side (n-middle)
    for leftIdx= 0 to middle -1
        left_half[leftIdx] = data[leftIdx]
    for leftIdx= middle to n-1
        right_half[i-middle] = data[i]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(left_half, right_half, data)
}

merge(left_half, right_half, data)
{
    len_left_half = length(left_half)
    len_right_half = length(right_half)
    i,rightIdx,dataIdx = 0,0,0
    while (leftIdx< len_left_half && rightIdx < len_right_half)
        if (L[leftIdx] <= R[rightIdx])
            data[dataIdx] = L[leftIdx]
            leftIdx= i+1
        else
            data[dataIdx] = r[rightIdx]
            rightIdx = rightIdx + 1
        dataIdx = dataIdx + 1
    while(leftIdx< len_left_half)
        data[dataIdx] = L[leftIdx]
        leftIdx= leftIdx+ 1
        dataIdx = dataIdx + 1
    while(rightIdx < len_right_half)
        data[dataIdx] = R[rightIdx]
        rightIdx = rightIdx +1
        dataIdx = dataIdx +1
}
'''


def merge_sort(data):
    n = len(data)
    if (n < 2):
        return  # based condition
    middle = n // 2
    left_half = data[0:middle]  # up to but not including middle
    right_half = data[middle:]  # from middle to end of array
    for leftIdx in range(0, middle - 1):  # leftIdx= 0 to middle -1
        left_half[leftIdx] = data[leftIdx]
    for rightIdx in range(middle, n - 1):  # leftIdx= middle to n-1
        right_half[rightIdx - middle] = data[rightIdx]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(left_half, right_half, data)


def merge(left_half, right_half, data):
    len_left_half = len(left_half)
    len_right_half = len(right_half)
    leftIdx, rightIdx, dataIdx = 0, 0, 0
    while (leftIdx < len_left_half and rightIdx < len_right_half):
        if (left_half[leftIdx] <= right_half[rightIdx]):
            data[dataIdx] = left_half[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = right_half[rightIdx]
            rightIdx += 1
        dataIdx += 1
    while(leftIdx < len_left_half):
        data[dataIdx] = left_half[leftIdx]
        leftIdx += 1
        dataIdx += 1
    while(rightIdx < len_right_half):
        data[dataIdx] = right_half[rightIdx]
        rightIdx += 1
        dataIdx += 1


print('Unsorted list', data)
merge_sort(data)
print('Sorted list', data)

'''
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for leftIdxin range(0, n1):
        L[leftIdx] = arr[l + i]

    for rightIdx in range(0, n2):
        R[rightIdx] = arr[m + 1 + rightIdx]

    # Merge the temp arrays back into arr[l..r]
    leftIdx= 0     # Initial index of first subarray
    rightIdx = 0     # Initial index of second subarray
    dataIdx = l     # Initial index of merged subarray

    while leftIdx< n1 and rightIdx < n2:
        if L[leftIdx] <= R[rightIdx]:
            arr[dataIdx] = L[leftIdx]
            leftIdx+= 1
        else:
            arr[dataIdx] = R[rightIdx]
            rightIdx += 1
        dataIdx += 1

    # Copy the remaining elements of L[], if there
    # are any
    while leftIdx< n1:
        arr[dataIdx] = L[leftIdx]
        leftIdx+= 1
        dataIdx += 1

    # Copy the remaining elements of R[], if there
    # are any
    while rightIdx < n2:
        arr[dataIdx] = R[rightIdx]
        rightIdx += 1
        dataIdx += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Driver code to test above
data = [10, 15, 4, 23, 1, 2, 4]
n = len(data)
print("Given array is", data)


mergeSort(data, 0, n - 1)
print("\n\nSorted array is", data)
'''
