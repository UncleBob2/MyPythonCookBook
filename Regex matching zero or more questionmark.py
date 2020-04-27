import re

#Matching Zero or More with the Question Mark ?
batRegex = re.compile(r'Bat(wo)?man')
batRegex.search('The Adventures of Batman')
print(batRegex.search('The Adventures of Batman'))
#'Batman'


batRegex.search('The Adventures of Batwoman')
print(batRegex.search('The Adventures of Batwoman'))
#'Batwoman'
