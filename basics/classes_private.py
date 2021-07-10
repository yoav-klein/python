
class Base():
    def say_hi(self):
        print("Hi from Base")

    def __init__(self):
        self.__say_hi()
    
    __say_hi = say_hi
    

class Derived(Base):
    def say_hi(self):
        print("Hi from derived")

d = Derived()