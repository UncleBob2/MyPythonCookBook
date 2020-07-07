''' scan the array from left to right, bubble to the largest number to the right

for k = 1 to n-1
{
    for i 0 to n-2
        {
        if A[i] > A[i+1]
            swap(A[i], A[i+1])
        }
}
'''
A_list = [7, 2, 5, 4, 9, 2]
#A_list = [34, 5, 6, 81, 0, 5]
#A_list = [2, 7, 4, 1, 5, 3]


print('Unsorted A_list', A_list)
for k in range(1, len(A_list) - 1):
    for i in range(len(A_list) - 1): # based on sudo code above where by k start from 1 and i from 0
        if A_list[i] > A_list[i + 1]:
            A_list[i], A_list[i + 1] = A_list[i + 1], A_list[i]
print("Sorted A_list", A_list)


# for i in range(0, len(A_list) - 1):
#     for j in range(0, len(A_list) - 1 - i):
#         if A_list[j] > A_list[j + 1]:
#             A_list[j], A_list[j + 1] = A_list[j + 1], A_list[j]

# print(A_list)
