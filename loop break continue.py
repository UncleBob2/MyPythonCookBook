
nums = [1,2,3,4,5]

for num in nums:
    print('sequence 1', num)

for num in nums:
    if num ==3:
        print('break condition')
        break
    print('break in seq',num)


for num in nums:
    if num ==3:
        print('continue condition')
        continue
    print('continue in seq, skip to next iteration',num)

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1


