
class Person:
    name = "blah"

    def getName(self):
        print("The name of the person is %s" % self.name)

myperson = Person()

print(myperson.name)
myperson.getName()


class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle()
car1.color = "Green"
car1.name = "Kadilak"

car2 = Vehicle()
car2.color = "Black"
car2.name = "Mazda"

print(car1.description())
print(car2.description())
