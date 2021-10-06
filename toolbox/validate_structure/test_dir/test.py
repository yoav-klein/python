

class A:
    def __init__(self):
        self.i = 10

    def display(self):
        print(self.i)

    def non_object_function():
        print("Call me with no object !")

a = A()
a.i = 11
A.non_object_function()
a.display()
A.display(a)


# class A:
#     names = ["Joe"]
    
# a = A()
# print(a.names is A.names)
# A.names.append("Bob")

# print(A.names)
# print(a.names is A.names)


#a = A()
#a.names.append("Benny")

#print(A.names)
#print(A.names is a.names)

#A.name= "Benny"
#print(a.name)

#print(a.name is A.name)

# a.name = "Benny"
# print(a.name is A.name)

