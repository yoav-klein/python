class Dog:
    tricks = []             # mistaken use of a class variable
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
    def add_trick(self, trick):
        self.tricks.append(trick)
    def print_dog(self):
        print(f"I'm {self.name}, and I'm {self.age} years old")

d1 = Dog('Bob')
d2 = Dog('Ray')

d1.add_trick("Jump")
d2.add_trick("Bend")

print(d2.tricks)

d3 = Dog('Charles', 10)
d3.print_dog()

class A:
    static_attr = 'Static'
    def __init__(self):
        self.object_attr = 'Objective'
    
    def change_static(self, val):
        self.static_attr = val
        
a1, a2 = A(), A()
a1.change_static("Something")
print(a2.static_attr)


class A:
    def __init__(self, a):
        self._a = a
    def func():
        print("Function in A")
    def method(self):
        print("The value of this object is:", self._a)

a = A(12)
a.method()
A.func()