'''
Desc:
    Python map() function to apply on a list iterable
'''

a = {'x': 'John', 'y':'Wick'}  # input stored in variable a.
print("{x}'s last name is {y}".format_map(a))  # Use of format_map() function

b = {'name':"George", 'mesg': '10'}
print('{name} has {mesg} new message'.format_map(b))

name = "Fred"
print("He said his name is {name!r}.")

magic = '{0}{1}{0}'.format('abra', 'cad')
print(magic)

print('Hi %s, I have %d donuts. Woud you like to have %d?'%('Alice',32,3))
