def h_func():
    return 'Hello World!' # return the string hello world

print(h_func)
print(h_func())

print(h_func().upper())


def h_func(greeting, name = 'You'): # default value for name
    return '{}, {}'.format(greeting, name)

print(h_func('Hi'))

print(h_func('Hi', 'Bob'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = 'John', age =22)

courses = ('Math', 'Art')
info = {'name': 'John', 'age': 22}

student_info(courses, info) # will not give us the desired results
student_info(*courses, **info) # correct info
