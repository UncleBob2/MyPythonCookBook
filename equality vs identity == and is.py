# what is the difference between "==" and "is"?
# "==" checks for equality (subjective)
# "is" checks for identity (some object in memory)

'''
'coke' == 'pepsi'   false
'pepsi' == 'pepsi' true (subjective)
'pepsi' is 'pepsi' only true if same object
if lemon in pepsi, and one without lemon
pepsi == pepsi True
pepsi is pepsi FALSE
'''


l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]
l3 = l2

print('memory location', id(l1))
print('memory location', id(l2))
print('memory location', id(l3))
print(id(l1) == id(l2))
print(id(l3) == id(l2))

if l1 is l2:  # is checking if the memory address is equal
    print("l1 is l2 : ", True)
else:
    print("l1 is l2 : ", False)

if l1 == l2:
    print("l1 == l2 : ", True)
else:
    print("l1 == l2 : ", False)

if l3 is l2:
    print("l3 is l2 : ", True)
else:
    print("l3 is l2 : ", False)

if l3 == l2:
    print("l3 == l2 : ", True)
else:
    print("l3 == l2 : ", False)
