#Dot-Star (.*) greedy vs. Non Greedy (.*?)
import re
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))  #'Al'
print (mo.group(2)) #'Sweigart'
#Matching Newlines with the Dot Character  re.compile('.*', re.DOTALL)
newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
'Serve the public trust.\nProtect the innocent.\nUphold the law.'
