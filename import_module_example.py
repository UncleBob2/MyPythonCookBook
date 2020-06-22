# this is an example module

print('Imported the example module...')

test = 'Test String from example module'

def find_index(to_search, target):
    '''Find the index of a value in sequence.'''
    for i, value in enumerate(to_search):
        if value ==target:
            return i

    return -1

