

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


print("----------- Function with default values ----------")

def ask_ok(prompt, retries = 4, reminder = "Please try again !"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'yeah'):
            return True
        elif ok in ('n', 'no', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

print(ask_ok("Are you ok?", 2))


def print_car(type, year, **keywords):
    print("Your car is %s from year %s" % (type, year))

print_car(type= "Toyota", year= '2001')

my_toyota = {
    'type': 'Toyota',
    'year': '2001'
}

print_car(**my_toyota)

print("---------- keyword and positional paramteres -------------")
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)

print("------- **keywords -----------")

def print_person(name, age, **properties):
    print("Your name is", name, "And you are", age, "Years old")
    print("Other than that, you are:")
    for prop in properties:
        print(prop, ":", properties[prop])

print_person(name="Yoav", age=35, profession='Software engineer', city="Karmiel")

print("------------- *positionals ---------")

def printf(intro, *words):
    print(intro)
    for word in words:
        print(word, end = ", ")
    print()

printf("I would like to say these words", "carrot", "house", "monty python", "eliyahu")


def pos_or_kwd(name):
    print(name)

def position_only(name, /):
    print(name)

def kwd_only(*, name):
    print(name)

pos_or_kwd("Yoav")
pos_or_kwd(name="Yoav")

position_only("Yoav")
# this won't work:
# position_only(name="Yoav")

kwd_only(name="Yoav")
# this won't work:
# kwd_only("Yoav")

#--------- Unpacking multiple values from list to pass to a function ---------------

def average(first, second, third):
    return (first + second + third) / 3

values = [4, 5, 6]
print(average(*values))

values = {
    'first': 4,
    'second': 5,
    'third': 6
}



def print_car2(type, year, **keywords):
    print("Your car is %s from year %s" % (type, year))
    print("more details:")
    for keyword in keywords:
        print(keyword, keywords[keyword])

my_toyota2 = {
    'type': 'Toyota',
    'year': '2001',
    'color': 'Blue',
    'num_sits': 4
}

print_car2(**my_toyota2)
