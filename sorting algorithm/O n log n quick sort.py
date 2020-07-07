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

'''
#A_list = [7, 2, 5, 66, 3, 4, 9, 2]
A_list = [17, 41, 5, 22, 54, 6, 29, 3, 13]
# A_list = [34, 5, 6, 66, 99, 81, 0, 5]
# A_list = [34, 5, 6, 66, 99, 81, 0, 5]
# A_list = [10, 15, 4, 23, 88, 1, 2, 4]
# A_list = [10, 15, 4, 23, 1, 2, 4]
#


def Quick_sort(A_list, start, end):
    if (start < end):
        pIndex = partition(A_list, start, end)
        Quick_sort(A_list, start, pIndex - 1)
        Quick_sort(A_list, pIndex + 1, end)


def partition(A_list, start, end):
    pivot = A_list[end]
    pIndex = start
    for i in range(start, end):
        if (A_list[i] <= pivot):
            A_list[i], A_list[pIndex] = A_list[pIndex], A_list[i]
            pIndex += 1
    A_list[pIndex], A_list[end] = A_list[end], A_list[pIndex]
    return pIndex


print('Unsorted list', A_list)
Quick_sort(A_list, 0, 8)
print('Sorted list', A_list)


'''
def quick_sort(A_list):
    quick_sort2(A_list, 0, len(A_list) - 1)


def quick_sort2(A_list, low, hi):
    if low < hi:
        p = partition(A_list, low, hi)
        quick_sort2(A_list, low, p - 1)
        quick_sort2(A_list, p + 1, hi)


def get_pivot(A_list, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if A_list[low] < A_list[mid]:
        if A_list[mid] < A_list[hi]:
            pivot = mid
    elif A_list[low] < A_list[hi]:
        pivot = low
    return pivot


def partition(A_list, low, hi):
    pivotIndex = get_pivot(A_list, low, hi)
    pivotValue = A_list[pivotIndex]
    A_list[pivotIndex], A_list[low] = A_list[low], A_list[pivotIndex]
    border = low

    for i in range(low, hi + 1):
        if A_list[i] < pivotValue:
            border += 1
            A_list[i], A_list[border] = A_list[border], A_list[i]
    A_list[low], A_list[border] = A_list[border], A_list[low]

    return(border)


print('Unsorted list', A_list)
quick_sort(A_list)
print('Sorted list', A_list)
'''
