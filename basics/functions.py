
# ----- Simple function with parameter
def fibbonaci(n):
    "This is a docstring"
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b

# fibbonaci(20)

# ---- Fibonnaci that returns a value

def fibbonaci(n):
    "This fibbonaci returns a list with the values"
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    
    return result

fib = fibbonaci(40)
print(fib)


# ------ variables are usually local
# You can override a global variable with a local one
# you can also modify a global using the global keyword

name = "Yoav"

def say_hi():
    # global name
    name = "Dikla"
    print("Hi" + ' ' + name)

say_hi()
print("The name now is: %s" % name)


