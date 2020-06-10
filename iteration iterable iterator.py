# iteration is a process. Any time you use a loop to go over a group of item
# iterable is an object that can be use in an interation
# iterator is an object with  __next__ method
# useful built-in functions of iterables: sum, sorted, any, all, max, min
for elementInList in [1, 2, 3]:
    print(elementInList)
print()
for elementInTuple in (1, 2, 3):
    print(elementInTuple)
print()

for key_Dic in {'one':1, 'two':2}:
    print(key_Dic)

for elementInSet in {7,1,9}:
    print(elementInSet)

for charInString in "123":
    print(charInString)
print()

for line in open("oceans.txt"):
    print(line, end='')