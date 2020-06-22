# Sets = don't care about order, different order each run
# use set to remove duplicate value
# Membership test i.e. more efficent to determine if an element is part of a set

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)

print('Set is best for Membership test, Is "Math" in set? ', 'Math' in cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print('Find similar elements between two sets', cs_courses.intersection(art_courses))
print('Find different elements between two sets', cs_courses.difference(art_courses))
print('Union of two sets', cs_courses.union(art_courses))

# creating empty set
empty_set = set() # can't use empty_set = {}. This is for dictionary
