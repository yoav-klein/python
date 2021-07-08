
print("This is module1 in subpackage1")
# absolute import
# import package1.module2

# relative import
from . import module2
module2.function1()

# from .module2 import function1
# function1()

