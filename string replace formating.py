#Print Welcome Message

message = 'Hello World!'
#slicing string
print(message[6:])
#count number of letter 'l'
print(message.count('l'))
#print all upper case
print(message.upper())
#count the index of the word within a string, return -1 if not in variable
print(message.find('World'))

new_message = message.replace('World', 'Universe')
print(new_message)

# using formated string
greeting = 'Hello'
name = 'Michael'
city = 'Calgary'
message = '{}, {}. Welcome to {}!'.format(greeting, name, city)
print(message)

# using f string in python 3.6 or higher
message = f'{greeting}, {name.upper()}. Welcome to {city}!'
print(message)

# show all available string formating
print(dir(name))

print(help(str.find))
