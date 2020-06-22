# user.py
from library import Base


assert hasattr(Base, 'foo'), "importing libary is broken, you fool!"

class Derived(Base):
    def bar(self):
        # return 'bar'
        return self.foo()

