# module_b

print("---- module B ------")
import module_a
module_a.functionA()

# from module_a import functionA
import sys
print(dir(sys.modules["module_a"]))
print(dir(module_a))


def functionB():
    print('Hello, World!')
    print(dir(module_a))
    module_a.functionC()