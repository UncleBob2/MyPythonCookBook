'''
writing functions without global variables is encouraged, you usually don’t have
to worry about the function’s code interacting with the rest of your program
'''


def spam():
    eggs = 'spam local 2'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local 1'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

def hotdog():
    global eggs #changing global variable with local func
    eggs = 'spam'


eggs = 'global'
bacon()
print(eggs) # prints 'global'
hotdog()
print(eggs)