#library.py

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if not 'bar' in body:
            raise TypeError("Bad user class, missing bar")
        return super().__new__(cls, name, bases, body)



class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()
