# This program says hello and asks for your name and age

print('Hi there!, #asking for user\'s input from the line below')
print('What is your name?')  # ask for their name
my_name = input()
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name))
print('what is your age?')  # ask for their age
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')



# Below is a shorter coding for user's input and print

print('#Asking for user\'s input on the same line')
name = input('what is your name? ')
print('Hello ' + name)

number = input('What is your favorite number? ') # Get a number from the user
triple = int(number)*3
print('Your number multiplied by three is '+ str(triple))



