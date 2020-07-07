A_list = [7, 2, 5, 66, 3, 4, 9, 2]
#A_list = [34, 5, 6, 66, 99, 81, 0, 5]
#A_list = [10, 15, 4, 23, 88, 1, 2, 4]
#A_list = [10, 15, 4, 23, 1, 2, 4]
# recursive, O(nlogn)

# Python program for implementation of MergeSort
'''
1) divide and conquer
2) recursive
3) stable - equal keys = relative order same as the original list (1,2), (2,5), (4,8), (2,3) => (1,2), (2,5), (2,3), (4,8)
4) not In-Place - extra memory is required

merge_sort(A_list)
{
    n = length(A_list)
    if (n < 2) return # based/exit condition
    mid = n //2
    left_half = array of size (mid)
    right_half = array of side (n-mid)
    for i = 0 to mid -1
        left_half[i] = A_list[i]
    for i = mid to n-1
        right_half[i-mid] = A_list[i]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(left_half, right_half, A_list)
}

merge(left_half, right_half, A_list)
{
    nL = length(left_half)
    nR = length(right_half)
    i,j,k = 0,0,0
    while (i < nL && j < nR)
        if (L[i] <= R[j])
            A_list[k] = L[i]
            i = i+1
        else
            A_list[k] = r[j]
            j = j + 1
        k = k + 1
    while(i < nL)
        A_list[k] = L[i]
        i = i + 1
        k = k + 1
    while(j < nR)
        A_list[k] = R[j]
        j = j +1
        k = k +1
}
'''


def merge_sort(A_list):
    n = len(A_list)
    if (n < 2):
        return  # based condition
    mid = n // 2
    left_half = A_list[0:mid]  # up to but not including mid
    right_half = A_list[mid:]  # from mid to end of array
    for i in range(0, mid - 1):  # i = 0 to mid -1
        left_half[i] = A_list[i]
    for i in range(mid, n - 1):  # i = mid to n-1
        right_half[i - mid] = A_list[i]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(left_half, right_half, A_list)


def merge(left_half, right_half, A_list):
    nL = len(left_half)
    nR = len(right_half)
    i, j, k = 0, 0, 0
    while (i < nL and j < nR):
        if (left_half[i] <= right_half[j]):
            A_list[k] = left_half[i]
            i += 1
        else:
            A_list[k] = right_half[j]
            j += 1
        k += 1
    while(i < nL):
        A_list[k] = left_half[i]
        i += 1
        k += 1
    while(j < nR):
        A_list[k] = right_half[j]
        j += 1
        k += 1


print('Unsorted list', A_list)
merge_sort(A_list)
print('Sorted list', A_list)

'''
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

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
A_list = [10, 15, 4, 23, 1, 2, 4]
n = len(A_list)
print("Given array is", A_list)


mergeSort(A_list, 0, n - 1)
print("\n\nSorted array is", A_list)
'''
