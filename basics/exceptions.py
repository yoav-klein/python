

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
def chain():
    try: 
        raise OSError("What a problem that is..")
    except Exception as e:
        raise Base(e.args[0]) from e

#try:
chain()
#except Base as e:
#    print(e)

print("--------- finally ----------")

def bool_return():
    try:
        return True
    finally:
        return False


print(bool_return())
