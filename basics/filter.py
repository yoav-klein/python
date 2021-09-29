
"""
An example of using the filter() function

This function takes an iterable and a function, and returns a new iterator
that contains only the elemets to which function returns true
"""



def is_in_family(name):
    family = ["yoav", "dikla", "tamar", "roni"]
    if name in family:
        return True
    else:
        return False


some_names = ["yoav", "dikla", "moshe", "tamar", "roni"]
only_family = list(filter(is_in_family, some_names))

print(only_family)

