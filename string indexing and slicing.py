# >>> spam = 'Hello world!'
# >>> spam[0]
# 'H'
# >>> spam[4]
# 'o'
# >>> spam[:5]
# 'Hello'
# >>> spam[6:]
# 'world!'

spam = "python"
print('# Iterate over the string without indexing')
for value in spam:
   print(value, end='')


print()

print('\n # Iterate over the string using indexing')
for value in range(0,len(spam)):
    print(spam[value], end='')

print()

print('\n # Iterate over the string using enumerate type')
for value,char in enumerate(spam):
    print(char, end='')
print('\n\n')

print('\n # String Slicing from index 2 to 6 ')
for value in range(2,6):
    print(spam[value], end='')

print('\n')
# 
# p
# py
# pyt
# pyth
# pytho
# python

for i in range(6):
    for value in range(i+1):
        print(spam[value], end='')
    print()