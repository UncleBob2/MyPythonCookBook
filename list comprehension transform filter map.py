# List comprehesions: sometimes a programming design pattern becomes common enough to warrant its own special syntax
# List comprehensions are a tool for transforming one list (any iterable actually) into another list.
# During this transformation, elements can be conditionally included in the new list and each element can be transformed as needed.
# Every list comprehension can be rewritten as a for loop but not every for loop can be rewritten as a list comprehension.
'''
Anew_things = [] #A creating a new list where elements can be conditionally included or transformed
for ITEM in old_things: # C
    if condition_based_on(ITEM): # D
        new_things.append("Bsomething with " + ITEM) # B

Anew_things = ["Bsomething with " + ITEM  for ITEM in old_things if condition_based_on(ITEM)]  #list comprehension
'''

numbers = [1,2,3,4,5,6]
odd_numbers=[]  #a
for number in numbers: #c
    if number %2 ==1: #d
        odd_numbers.append(number) #b
print('Odd numbers using for loop', odd_numbers)

numbers = [number for number in numbers if number %2 ==1]
print('Odd numbers using list comprehension', odd_numbers)

doubled_numbers =[] # list comprehesion without if condition
for n in numbers:
    doubled_numbers.append(n*2)

doubled_numbers = [n*2 for n in numbers]
print('Double number list comprehension', doubled_numbers)

matrix=[(0,1,2),
        (3,4,5),
        (6,7,8)]

flattened =[]
for row in matrix:
    for n in row:
        flattened.append(n)

flattened = [n for row in matrix for n in row]
print('list comprehension print', flattened)

print()
# lets say that we have a huge list and would like to find all the movies start with letter g
movies = [('Star wars',1941), ('Gandhi',2001),( 'Casablanca',1923),( 'Gone with the wind',1977),
          ('No Country for Old Men', 2007), ('The Aviator', 2004), ( 'Citizen kane',1944)]

gmovies = []  # A
for title in movies: #C
    if title[0].startswith('G'): #D
        gmovies.append(title)
print('Movies with letter G at begining', gmovies)

gmovies = [title for title in movies if title[0].startswith('G')] #list of tuples
print('Movies with letter G at begining', gmovies)

gmovies = [title for title in movies if title[1] < 2000] #list of tuples
print('Movies released before 2000', gmovies)
print()

# squares = []  # creating a square list using for loop vs commprehension
# for i in range(1,10):
#    squares.append(i**2)

square_num = [i**2 for i in range(10)]
print('Populate square number list with comprehension: ', square_num)

print()

#Nesting Comprehension
# This creates a 3x4 "matrix" (list of lists) of zeros.
mat3_4 =[]
for col in range(4):
    for row in range(3):
        mat3_4.append(0)

#mat3_4= [[0 for col in range(4)] for row in range(3)]
print('Populating 4 x 3 matrix: ', mat3_4)
print()

# find word with letter o using list comprehension
word_collection = ['Python', 'Like', 'You', 'Mean', 'It']
words_with_o = []
# for word in word_collection:
#     if "o" in word.lower():
#         words_with_o.append(word)

words_with_o = [word for word in word_collection if "o" in word.lower()]
print(words_with_o)

# creating a tuple using a comprehension expression
square= tuple(i**2 for i in range(5)) #(0, 1, 4, 9, 16)
print(square)

# for scaler vector multiplication v[] *4
v = [2,-3,1]
w =[]
for x in v:
    w.append(4*x)

w = [4*x for x in v ]
print('scalar vector result', w)

# # Cartesian product example
# A={1,3} and B = {x,y}
# A x B = {(1,x), (1,y), (3,x), (3,y)}

A = [1,3,5,7]
B = [2,3,6,8]
cartesian_product =[]
for a in A:
    for b in B:
        cartesian_product.append((a,b))

print(cartesian_product)

cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)

