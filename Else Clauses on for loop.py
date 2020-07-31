def find_index(data, target):
    for i, value in enumerate(data):
        if value == target:
            break
    else:
        return -1
    return i


data = ['Corey', 'Rick', 'John']
index_location = find_index(data, 'Rickxx')

print('Location of target index: {}'.format(index_location))

print()
my_list = [1, 2, 3, 4, 5]

for i in my_list:
    print(i)
    if i == 5:  # if 3, then break out of loop, if larger 5 then no break, if == 5 break
        break
else:  # no break
    print('Loop hits the For/Else Statement')

print('\n\nwhile loop else')
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 5:  # if 3, then break out of loop, if larger 5 then no break, if == 5 break
        break
else:
    print('Loop hits the While/Else Statement')
