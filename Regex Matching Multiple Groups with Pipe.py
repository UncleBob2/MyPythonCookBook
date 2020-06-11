import re

heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
print(mo1.group())
#output 'Batman'


mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()
print(mo2.group())
#output 'Tina Fey'
