
from typing import Callable, List

def greeting(name: str) -> str:
    print(greeting.__annotations__)
    return f"Hello {name}"


# first version - no type hints
# def factorial(i):
#     if i < 0:
#         return None
#     if i == 0:
#         return 1
#     if i > 0:
#         return i * factorial(i - 1)

# second version - type hints

def factorial(i: int) -> int:
    if i < 0:
        return None
    if i == 0:
        return 1
    if i > 0:
        return i * factorial(i - 1)

def map_int_list(fnc: Callable, lst: List[int]) -> List[int]:
    return [fnc(i) for i in lst]

print(map_int_list(factorial, [1, 2, 3]))