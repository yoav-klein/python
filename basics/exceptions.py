

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops.. that's not an integer")


class Base(Exception):
    pass

class Derived(Base):
    pass

try:
    raise Derived()
except Base:
    print("Caught Base")
except Derived:
    print("Caught Derived")


# args
try:
    raise Base('What', 'TheHeck')
except Base as err:
    print(err.args)
    print(err)


def this_fails():
    raise Base()

try:
    this_fails()
except Base:
    print("Base caught!")

# print("------ exception chaining ------")
# try: 
#     this_fails()
# except Base as b:
#     raise IOError from b

print("--------- finally ----------")

def bool_return():
    try:
        return True
    finally:
        return False


print(bool_return())