
a = [1, 2, 'green', 4, 5, 1, 'green', 3, 4, 5, 1]
for i, val in enumerate(a):
    if val == 'green':
        a[i] = 10

print(a)
