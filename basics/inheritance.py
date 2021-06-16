

class Mamal:
    def make_sound(self):
        self.make_your_sound()
    
    def make_your_sound(self):
        print("Ahhmm..")


class Human(Mamal):
    def make_your_sound(self):
        print("Hello")

class Dog(Mamal):
    def make_your_sound(self):
        print("Woof!!")


m = Human()
m.make_sound()