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



# String format()  - allows you to format selected parts of a string.
#Format the price to be displayed as a number with two decimals:
price1 = 12.3434
price2 = 12.3434
txt = "The incorrect price is {} and the correct price is {:.2f} dollars"
print(txt.format(price1,price2))


#If you want to use more values, just add more values to the format() method:
#placeholders(curly brackets {}) in the text
price = 49.34
quantity = 3
itemno = 567

myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index Numbers, you can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
price = 9.78    # assigned {2} index
quantity = 2  # assigned {0} index below
itemno = 5667  # assigned {1] index below

myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


#if you want to refer to the same value more than once, use the index number:
age = 36     # assigned {0} index below
name = "John"   # assigned {1} index below
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


#String Methods - All string methods returns new values. They do not change the original string.

'''
Method	Description
capitalize()    	Converts the first character to upper case
casefold()      	Converts string into lower case
center()        	Returns a centered string
count()         	Returns the number of times a specified value occurs in a string
encode()        	Returns an encoded version of the string
endswith()      	Returns true if the string ends with the specified value
expandtabs()    	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()       	Returns True if all characters in the string are alphanumeric
isalpha()   	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()       	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()       	Returns True if all characters in the string are whitespaces
istitle()       	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()         	Converts a string into lower case
lstrip()        	Returns a left trim version of the string
maketrans()     	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()        	Splits the string at the specified separator, and returns a list
rstrip()        	Returns a right trim version of the string
split()         	Splits the string at the specified separator, and returns a list
splitlines()    	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        -remove the space beginning and end; hence, returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()         	Converts a string into upper case
zfill()         	Fills the string with a specified number of 0 values at the beginning
'''
