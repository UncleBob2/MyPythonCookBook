# Lambda Expressions = Anonymous Function  (throw away functions, for sorting and filtering data) – Function in a single line
# write a function to compute 3x+1
def f(x):
    return 3*x +1
print('function',f(7)) #22

# alternative implement with lamda function with a given name g
g = lambda x: 3*x +1
print('lambda',g(7)) #22

print()
# Lambda with multiple inputs - combine first and last name into a single full name
# first name = first input, last name second input, strip blank space and only the first letter is capitalized
full_name = lambda first_name, last_name: first_name.strip().title() + ' '+ last_name.strip().title()
print(full_name('  leonhear', 'EURLER')) #Leonhear Eurler

print()
# function that make functions
def quad_func(a,b,c):
    return lambda x: a*x**2 + b*x + c
f = quad_func(2,3,-5)
print(f(2)) #9  lambda is assign name f
print(quad_func(2,3,-5)(2)) #9 where no name is assigned to function

# x1, x2... are inputs
# lamdba x1, x2, x3,..., xn: <expression>

print()
# using lambda without giving it a name
# sort authors last name using lambda with key function and lower case
scifi_authors = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Orson Scott Card', 'Leigh Brackett']
print('Original author list:',scifi_authors)
# Because authors are in a list; hence, we can use sort
#help(scifi_authors.sort) # If a key function is given, apply it once to each list item and sort them,

                         # split the first and last name with space,index -1 to omit middle name and access last name
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower()) #conver the string to lower case so sorting is not case sensitive

print('Sorted authors by last name:', scifi_authors)


