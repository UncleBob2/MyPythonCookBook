import sys, os
# sys.path.append('/users/.....')

import random

courses = ['History', 'Math', 'Physics', 'CompSci']

print('print random.choice courses = ', random.choice(courses))

print('get the current working directory', os.getcwd())

print('print the location of the os file', os.__file__)

print('\nprint all the python paths ' , sys.path)


