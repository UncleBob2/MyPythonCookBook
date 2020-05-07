# a list comprehension is a syntax for constructing a list
# List comprehesions:
# [expr for val in collection]
# [expr for val in collection if <test1> and <test2>]
# [[expr for col in collection1] for row in collection2]
# [[0 for col in range(4)] for row in range(3)]

# lets say that we have a huge list and would like to find all the movies start with letter g
movies = [('Star wars',1941), ('Gandhi',2001),( 'Casablanca',1923),( 'Gone with the wind',1977),
          ('No Country for Old Men', 2007), ('The Aviator', 2004), ( 'Citizen kane',1944)]

gmovies = [title for title in movies if title[0].startswith('G')] #list of tuples
print('Movies with letter G at begining', gmovies)

gmovies = [title for title in movies if title[1] < 2000] #list of tuples
print('Movies released before 2000', gmovies)
print()
# create square number list
# long way
# squares = []
# for i in range(1,10):
#    squares.append(i**2)
# short way using list comprehension
square_num = [i**2 for i in range(10)]
print('Populate a new list with comprehension: ', square_num)

print()

#Nesting Comprehension
# This creates a 3x4 "matrix" (list of lists) of zeros.
mat3_4= [[0 for col in range(4)] for row in range(3)]
print('Populating 4 x 3 matrix: ', mat3_4)
print()

# find word with letter 0 using list comprehension
words_with_o = []
word_collection = ['Python', 'Like', 'You', 'Mean', 'It']
words_with_o = [word for word in word_collection if "o" in word.lower()]
print(words_with_o)

# creating a tuple using a comprehension expression
square= tuple(i**2 for i in range(5)) #(0, 1, 4, 9, 16)
print(square)

# for scaler vector multiplication using comprensive expression
v = [2,-3,1]
w = [4*x for x in v ]
print('scalar vector result', w)

# # Cartesian product example
# A={1,3} and B = {x,y}
# A x B = {(1,x), (1,y), (3,x), (3,y)}

A = [1,3,5,7]
B = [2,3,6,8]

cartesian_product = [(a,b) for a in A for b in B]
print(cartesian_product)