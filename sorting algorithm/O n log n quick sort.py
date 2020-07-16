# O (nlogn) - Average case running time
# 0 (n^2) - worst case running time but can use avoided using random
# better than merge sort because it is in place; hence, less memory is used
# uses pivot to partition into two list left and right
# Python program for implementation of MergeSort
'''
1) divide and conquer
2) recursive
3) unstable - equal keys=relative order same as the original list (1, 2), (2, 5), (4, 8), (2, 3)= > (1, 2), (2, 3), (2, 5), (4, 8)
4) In PLACE - extra memory is required
5) performance depends largely on the pivot seletion

quick sort starts by randomnly picking one ball, called a pivot. It then rearranges the other balls by comparing
them with the pivot. Larger number is moved to the right and smaller number is moved to the left. The pivot is placed
where it should be. Once the pivot is placed it split our data into two smaller unsorted set of data. Pick a pivot
rearrange the other balls, put back the pivot and so on.

'''
#data = [7, 2, 5, 66, 3, 4, 9, 2]
data = [67, 38, 71, 66, 72, 2, 47, 16, 67, 61, 59, 80, 14, 100,
        37, 50, 88, 23, 65, 68, 25, 44, 93, 92, 81, 94, 33, 88, 94, 9]
# data = [34, 5, 6, 66, 99, 81, 0, 5]
# data = [34, 5, 6, 66, 99, 81, 0, 5]
# data = [10, 15, 4, 23, 88, 1, 2, 4]
# data = [10, 15, 4, 23, 1, 2, 4]
#


def Quick_sort(data, low, high):
    if (low < high):
        border = partition(data, low, high)
        # left partition sort
        Quick_sort(data, low, border - 1)
        # right partition sort
        Quick_sort(data, border + 1, high)


def partition(data, low, high):
    pivotValue = data[high]
    border = low
    for i in range(low, high):
        if (data[i] <= pivotValue):
            data[i], data[border] = data[border], data[i]
            border += 1
    # swapping pivot element with border value
    data[border], data[high] = data[high], data[border]
    return border


print('Unsorted list', data)
Quick_sort(data, 0, len(data) - 1)
print('Sorted list', data)


'''
def quick_sort(data):
    quick_sort2(data, 0, len(data) - 1)


def quick_sort2(data, low, hi):
    if low < hi:
        p = partition(data, low, hi)
        quick_sort2(data, low, p - 1)
        quick_sort2(data, p + 1, hi)


def get_pivot(data, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if data[low] < data[mid]:
        if data[mid] < data[hi]:
            pivot = mid
    elif data[low] < data[hi]:
        pivot = low
    return pivot


def partition(data, low, hi):
    pivotIndex = get_pivot(data, low, hi)
    pivotValue = data[pivotIndex]
    data[pivotIndex], data[low] = data[low], data[pivotIndex]
    border = low

    for i in range(low, hi + 1):
        if data[i] < pivotValue:
            border += 1
            data[i], data[border] = data[border], data[i]
    data[low], data[border] = data[border], data[low]

    return(border)


print('Unsorted list', data)
quick_sort(data)
print('Sorted list', data)
'''
