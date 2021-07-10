

# call the functions from basics2 as a module
import basics2

lst = [1, 2, 3, 4, 5]
new_lst = basics2.rotate_left(lst)
print(new_lst)


# Create a function that checks if a certain name is in the global namespace.

def is_in_global_namespace(name):
    return name in globals()

a = 3
print(is_in_global_namespace('a'))
