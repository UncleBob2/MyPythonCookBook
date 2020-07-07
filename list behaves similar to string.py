# list operate exactly like string i.e. [1,2,'aaa'] + [3,4]
# b=a  (b is pointing to the list of a but b does not copy a)
# b = a[:] is actually a copy
# list a[1:3] works like string s[1:3]
# both string and list use indexing l[0], str[0]

a=[0,1,2,3,4]
print('Is three in the list a?', 3 in a)

google = 'google'
print('Is there a letter "g" in the word google?', 'g' in a)

a = ['ccc','aaaz','d','bb']
print('Custom sort by length',sorted(a,key=len)) #for the key, you don't pass any pameters.

def last(s):
    return s[-1]
print('Custom sort by last char',sorted(a,key=last)) #for the key, you don't pass any pameters.

b= ''.join(a)
print("Joined list a", b)


a = [0,1,2,3,4]
a.pop(0)
a.append(5)

for var in a:
    print(var)

