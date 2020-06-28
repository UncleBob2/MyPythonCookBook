# Duck tests - walk like a duck, quack like a duck - it must be a duck (sometime wrong but most time ok)
# Duck tests - we don't care if it is a duck or not. We just want it to behave like a duck.
# Easier to ask forgiveness than permission (EAFP) - not advised to check all the times for attritutes

class Duck:  # Duck & Person have some attributes but different class
    def quack(self):
        print('Quack, Quack')

    def fly(self):
        print('Flap, Flap!')


class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


def quack_and_fly(thing):
    print("\nNon - Pythonic: since we have to check attributes quack and fly")
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This passed the Duck tests but may not be a duck!')


def quack_and_fly_LBYL(thing):
    print("\nNon - Pythonic: LBYL - look before you leap")
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()  # very cumbersome method

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()


def quack_and_fly_EAFP(thing):
    print("\nEAFP(Pythonic) - just do it, if there is an error then deal with it")
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)


d = Duck()
quack_and_fly_LBYL(d)

p = Person()
quack_and_fly_LBYL(p)


def quack_and_fly(thing):
    print("\nPythonic: we don't care if the object is a duck. We just want it to behave like a duck.")
    thing.quack()
    thing.fly()

    print('')


d = Duck()
quack_and_fly_EAFP(d)

p = Person()
quack_and_fly_EAFP(p)
