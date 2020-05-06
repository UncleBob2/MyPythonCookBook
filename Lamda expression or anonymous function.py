# Lambda Expressions = Anonymous Function  (throw away functions, for sorting and filtering data) – Function in a single line
def f(x):
    return 3*x +1
print('function',f(7)) #22

# alternatively with lamda function
g=lambda x: 3*x +1
print('lambda',g(7)) #22

print()
# Lambda with 2 inputs
full_name = lambda first_name, last_name: first_name.strip().title() + ' '+ last_name.strip().title()
print(full_name('  leonhear', 'EURLER')) #Leonhear Eurler

print()
def quad_func(a,b,c):
    return lambda x: a*x**2 + b*x + c
f = quad_func(2,3,-5)
print(f(2)) #9
print(quad_func(2,3,-5)(2)) #9


print (lambda : "what is my purpose?") #<function <lambda> at 0x000002A3CC5904C0>
print (lambda x: 3*x + 1)
print (lambda x,y: (x*y)**0.5) # <function <lambda> at 0x000002A3CC5904C0>

print()
# sort authors last name using lambda with key function and lower case
scifi_authors = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Orson Scott Card', 'Leigh Brackett']
print('Original author list:',scifi_authors)
#help(scifi_authors.sort) # If a key function is given, apply it once to each list item and sort them,
                         #    ascending or descending, according to their function values.
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print('Sorted authors by last name:', scifi_authors)


