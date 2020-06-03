'''

condition = False

if condition:
    x = 1
else:
    x = 0

print(x)

'''
# 1) Ternary Conditionals - shorter if else
condition = True

x = 1 if condition else 0

print(x)

# 2) Underscore Placeholders - working large numbers

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(f'{total:,}')


# 3) Context Managers - automate managing resources i.e. closing files, multi-threads, or databases

with open('alice.txt', 'r') as f:
    file_content = f.read()

words = file_content.split(' ')
word_count = len(words)
print(word_count)

# 4) Enumerate - counter to looping over a list instead of counting

names = ['Corey', 'Chris', 'Dave', 'Travis']

for index, name in enumerate(names, start=1):
    print(index, name)

# 5) Zip - indexing multiple list at the same time
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')




# 6) Unpacking - 13:02
# 7) Setattr/Getattr - 19:08
# 8) GetPass - 26:24
# 9) Python dash m - 29:18
# 10) Help/Dir - 33:17