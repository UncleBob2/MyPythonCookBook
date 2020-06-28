# Duck tests - walk like a duck, quack like a duck - it must be a duck (sometime wrong but most time ok)
# Easier to ask forgiveness than permission (EAFP) - not advised to check all the times for attritutes

import os
my_file = "/tmp/test.txt"

# # Race Condition
# if os.access(my_file, os.R_OK): # sometime pass here but fail below
#     with open(my_file) as f:
#         print(f.read())
# else:
#     print('File can not be accessed')


# No Race-condition
try:
    f = open(my_file)
except IOError as e:
    print('File can not be accessed')
else:
    with f:
        print(f.read())
