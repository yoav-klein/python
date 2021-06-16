
# creating a simple class
class A:
    static_attr = 'Static'
    def __init__(self):
        self.object_attr = 'Objective'
    
    def print_value(self):
        print(self.object_attr)
    
    def change_static(self, val):
        self.static_attr = val
    


# referencing class attributes
print("Original value of A.static_attr is:", A.static_attr)
a1, a2 = A(), A()

print("a1.static_attr:", a1.static_attr)
print("a1.object_attr:", a1.object_attr)

# changing class attributes
A.static_attr = "YokoZona"
print("After changing A.static_attr, a1.static_attr:", a1.static_attr, "a2.static_attr:", a2.static_attr)

# call change_static for one of them, see what happens to the second
print("change a1.static_attr")
a1.change_static("Jerusalem")
print("a2.static_attr:", a2.static_attr)
# why that happened?  since what you did is to add a 'static_attr' attribute
# to the instance object, you didn't change the class attribute !

# but changing object_attr of one of them
a2.object_attr = "changed value"
print("after a2.object_attr changed: a1.object_attr", a1.object_attr)

# data attributes need not be declared. We can just reference them and they'll exist
a1.counter = 1
while a1.counter < 10:
    a1.counter = a1.counter * 2
print(a1.counter)
del a1.counter

# method objects
a1.print_value()
a1.object_attr = "Kakamaika"
print_a1 = a1.print_value
print_a1()

# you can also call a method like this
A.print_value(a2)

print(print_a1)

# try changing the print_value function
def new_function(self):
    print("This is the new version of print_value")
    print(self.object_attr)

A.print_value = new_function

a1.print_value()
# that will fail:
# a1.no_self() 


print("------------")
# assigning a function object defined outside a class to a class

def print_dog_def(self):
    print ("The type of %s is %self.type" % (self.name, self.type))

class Dog:
    def __init__(self, name, type):
        self.type = type
        self.name = name

    print_dog = print_dog_def

d = Dog("Bobby", "Lavrador")
d.print_dog()

class Number:
    def __init__(self, number):
        self.number = number
    
    def add(self, num):
        self.number = self.number + num

    def multiply(self, num):
        origin = self.number
        for i in range(num - 1):
            self.add(origin)
    
    def print(self):
        print("I am now", self.number)

five = Number(3)
five.add(6)
five.print()
five.multiply(4)
five.print()

