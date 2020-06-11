# d = { }  # declare dictionary && assigning individual elements
# d['a'] = 'alpha' #key = a, storage alpha at key a
# d['o'] = 'omega'
# count characters in a word
word = 'brontosaurus'
a_dict = {}
for char in word:  # word is string
    if char in a_dict:
        a_dict[char] += 1 # existing key's value is increment by 1
    else:
        a_dict[char] = 1 # assigning both key and value
print(a_dict)

# count a number of word occurrence in a paragraph
paragraph = 'We are not what we should be We are not what we need to be But at least we are not what we used to be'
a_dict={}
txt = paragraph.lower().split() # list of string
for word in txt:
    if word in a_dict:
        a_dict[word] += 1
    else:
        a_dict[word] = 1

print(a_dict)


frequency= { }
txt = paragraph.lower().split()
for item in txt:  # assigning dictionary key and values
    frequency[item] = txt.count(item)
print(frequency)

'''
This output format is also an input format. For example, you can create a new dictionary with three items:
>>> eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'} But if you print eng2sp, you might be surprised:

>>> print eng2sp
{'one': 'uno', 'three': 'tres', 'two': 'dos'}

The order of the key-value pairs is not the same. In fact, if you type the same example on your computer, you might get 
a different result. In general, the order of items in a dictionary is unpredictable.

But that’s not a problem because the elements of a dictionary are never indexed with integer indices. 
Instead, you use the keys to look up the corresponding values:
'''