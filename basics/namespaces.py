
######### Example: a is declared globally
a = 1

def func():
    print("--- func1 ----")
    # this 'a' here is local !
    a = 3
    print(a)

func()

# it didn't change global a
print(a)

######## Example: read a global in a function
def func2():
    print("---- func2 -----")
    # this will be the global a
    print(a)

func2()

##### Example: changing the global using global
def func3():
    print("------- func3 ------")
    global a
    a = 10

func3()
print(a)


###### Example: nested functions

def outer():
    print("---------- outer ---------")
    num = 4
    def inner():
        num = 20
        print("The value of num in inner is:", num)
    inner()
    print("The value of num in outer is:", num)

outer()

###### Example: changing the value of the outer from inner using nonlocal nested functions

def outer():
    print("---------- outer ---------")
    num = 4
    def inner():
        nonlocal num
        num = 20
        print("The value of num in inner is:", num)
    inner()
    print("The value of num in outer is:", num)

outer()


##### deleting 

def outer():
    print("---------- outer ---------")
    num = 4
    def inner():
        nonlocal num
        del num
    print("The value of num in outer is:", num)
    inner()
    try:
        print("The value of num in outer is:", num, "before deletion")
    except UnboundLocalError:
        print("Ahh.. it was deleted !")
        
outer()

#### refering to a local before it was declared raises an error

def not_good():
    print(x)
    x = 9