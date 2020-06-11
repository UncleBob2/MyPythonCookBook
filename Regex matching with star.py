#Matching Zero or More with the Star * vs Dot-Star .*
#The * (called the star or asterisk) means “match zero or more”
import re

batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()
#'Batwowowowoman'
