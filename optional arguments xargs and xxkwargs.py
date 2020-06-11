def spam(required, *args, **kwargs):
    print(required) # string
    if args:
        print(args) # tuple
    if kwargs:
        print(kwargs) # dictionary


# spam('required only''hello')
# spam('hello',1,2,3)
# spam('hello',1,2,3, key1='value', key2=999)


def wrapper(required, *args, **kwargs):
    kwargs['name']='Alice' # adding Alice to **kwards's dictionary
    new_args = args +('four',) # create new tuple and add four
    spam(required, *new_args, **kwargs)
    if args:
        pass
    if kwargs:
        pass

wrapper('hello',1,2,3, key1='value')


# Subclassing example
class Car:
    def __init__(self,color, mileage):
        self.color = color
        print(color)
        self.mileage = mileage
        print(mileage)


class AlwaysBlueCard(Car): # subclass of car
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 'blue'

print(AlwaysBlueCard('green',343))



