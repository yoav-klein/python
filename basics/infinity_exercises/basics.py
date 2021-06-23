
def is_even(num):
    """
    Write a function that determines whether or not a number is even
    """
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")

is_even(5)
is_even(6)


#####
def multiple_string(string, num):
    """ Create a function that receives a string and an integer
    and prints the string number of times
    """
    for i in range(num):
        print(string)

multiple_string("Yoav", 4)

#######
def is_leap_year(year):
    """
    Write a function that decides whether a year is a leap year. A leap year is
    - A multiply of 4
    - unless it's a multiply of 100
    - but a multiply of 400 is a leap year
    """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("This is a leap year")
    else:
        print("This is NOT a leap year")


is_leap_year(16)
is_leap_year(100)
is_leap_year(400)

def is_int(num):
    """Write a function that receives a parameter and determines
    whether or not it's a int
    """
    if(type(num) == int):
        print("Yesss... it's a int")
    else:
        print("Neiii...")

is_int(4)
is_int('c')

def flip_number(num):
    """Write a function that receives an integer and flips it
       1234 -> 4321
    """
    if(type(num) == str):
        num = int(num)
    sum = 0
    count = 0
    while num > 0:
        count += 1
        sum = sum * 10
        current = num % 10
        sum += current
        num = (int)(num / 10)
    
    return sum

print(flip_number(1234))
# print(flip_number(123.4))
print(flip_number("1234"))

def grade_category(grade):
    """Write a function that receives a grade between 0 - 100
    and translate it to letters between A - F
    """
    if 0 < grade <= 10:
       letter = 'F'
    if 10 < grade <= 30:
        letter = 'E'
    if 30 < grade <= 50:
        letter = 'D'
    if 50 < grade <= 70:
        letter = 'C'
    if 70 < grade <= 90:
        letter = 'B'
    if 90 < grade <= 100:
        letter = 'A'

    print("The letter of the grade is:", letter)

grade_category(10)
grade_category(49)
grade_category(70)

def factorial(num):
    """Write a factorial function
    """
    sum = 1
    for i in range(num):
        sum *= (i + 1)
    
    print(sum)

factorial(4)

def factorial_rec(num):
    """Write a factorial function
    that works recursively
    """
    if(num == 1):
        return 1

    return num * factorial_rec(num - 1)

print(factorial_rec(4))