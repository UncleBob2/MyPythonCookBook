import import_module_example

courses = ['History', 'Math', 'Physics', 'CompSci']

index = import_module_example.find_index(courses, 'Math')

print('result of function within the import_module_example ',index)


# more efficient
import import_module_example as mm
index = mm.find_index(courses, 'Math')
print('result of import import_module_example as mm ',index)

# less typing

from import_module_example import find_index, test
index = find_index(courses,'Math')
print('result of from import_module_example import_index ',index)
print(test)
