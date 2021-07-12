# module_a

print("----- module A ------")
import module_b

def functionA():
    print("This is functionA")

    module_b.functionB()
# from module_b import functionB
def functionB():
    pass

print(dir())
if __name__ == "__main__":
    print("Main")
    print(dir())
    functionA()

