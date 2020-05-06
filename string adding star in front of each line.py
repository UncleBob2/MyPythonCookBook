
print('Hello World!')
print('Welcome to my github')
print(r'c:\docs\navin')
print('navin\'s "laptop"')

# Code        	Result
# \'              Single Quote (escape character)
# \"              Double Quote (escape character)
# \\             	Backslash	(escape character)
# \n              Line
# \r              Carriage Return
# \t              Tab
# \b              Backspace
# \f              Form Feed
# \ooo            Octal value
# \xhh            Hex value
# {} - placeholder for string formating

import pyperclip

#text = pyperclip.paste()
#text = pyperclip.copy()

text = '''
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars'''

print('type for text var', type(text))
print('this is the clipboard: ', text)


lines = text.split('\n')  # converting string to a 'list' of string separate by \n
print('type for lines var', type(lines))
print('using text.split results: ', lines)
for i in range(len(lines)): #loop through all indexes in the 'lines' list and add star in front
    lines[i] = '* ' + lines[i] # add star to each string

lines = '\n'.join(lines) # convert a list of string values to a single string value
print('star added results: ', lines)

# * Lists of animals
# * Lists of aquarium life
# * Lists of biologists by author abbreviation
# * Lists of cultivars