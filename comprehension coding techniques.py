# comprehension apply to list, dictionary

nums = [1,2,3,4,5,6,7,8,9,10]

#task1 I want 'n' for each 'n' in nums
my_list =[]
for num in nums:
    my_list.append(num)
print('using for loop instead of comprehension',my_list)

comp_list = [n for n in nums]
print('using comprehension', comp_list)

#task2 I want n*n for each 'n' in nums
comp_list = [n*n for n in nums]
print('n*n using list comprehension', comp_list)

#task2 repeated but using a map and lambda (less readable)
lambda_list = map(lambda n: n*n, nums)
print('solution using map and lambda', list(lambda_list))

# task3 I want 'n' for each 'n' in nums if 'n' is even
even_comp = [n for n in nums if n%2 ==0]
print('using comprehension', even_comp)

# task3 repeated but using a filter and lambda
even_comp = filter(lambda n: n%2 ==0, nums) #(not as readable as above)
print('using filter and lambda', list(even_comp))

# task 4: I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
combined = [(letter, num) for letter in 'abcd' for num in range(4)]
print('comprehension with 2 for loop', combined)

# task 5: Dictionary comprehension - us curly bracket and semi colon for diction
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spidernam', 'Wolverine', 'Deadpool']
hero_ID = {name:hero for name, hero in zip(names, heros)}
print('Dictionary comprehension', hero_ID)

# task 6: if name not equal to Peter
hero_ID = {name:hero for name, hero in zip(names, heros) if name !='Peter'}
print('Dictionary comprehension without Peter', hero_ID)

# task 7: Set Comprehension - use curly bracket for set
nums = [1,1,2,2,3,3,4,5,5,5,5,6,6,6,7,8,7,7,9]
set_comp = {n for n in nums}
print('set comprehension', list(set_comp))


# task 8: Generator Comprehension - use round bracket
nums = [1,2,3,4,5,6,7,8,9,10]

my_gen = (n*n for n in nums)

print('generator comprehension',list(my_gen))

