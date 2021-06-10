

# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append(3)
# mylist.append("Yoav")
# print(mylist[0])

# for x in mylist:
#    print(x)

# number = 1 + 2 * 3 / 4.0
# print(number)

# string = "hello" + " " + "world"
# print(string)

# even_numbers = [2, 4]
# odd_numbers = [1, 3]

# print(odd_numbers + even_numbers)

print("hello", "yoav")

x = 4
if x == 4:
    print(x)
else:
    print("wow..")

name = "Yoav"
print("Hello, %s" % name)

age = 35
print("%s, you are already %d years old !" % (name, age))


# Conditions
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick")
else:
    print("its neither John or Rick")

 # is opertaor checks not the value equality, but whether it is the same object

x = 4
y = x
if(x is y):
    print("x and y are same object")


# String opertaions
astring = "Hello World !"
print(len(astring))
print(astring.index("o"))
print(astring[3:6])


#--------------------
# Loops
#-----------------
# There are for and while in python

print ("------ Loops --------")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# using the range() function.
list = range(2, 5)
for num in list:
    print(num)

# while
print("---- while ----")
count = 0
while count < 5:
    print(count)
    count += 1

# ----------------------
# Functions
# --------------------
print("----- Functions -----")

def my_function():
    print("This is a function")

def function_with_parameters(name, age):
    print("Hello %s, you are %d years old" % (name, age))

def add(first, second):
    return first + second

function_with_parameters("Yoav", 35)

print("3 + 5 is %d" % add(3, 5))