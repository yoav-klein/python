
# Create a list containing all squared numbers between 0 - 100

def test_squared_numbers():
    print("------- Squared numbers ---------")
    squared_numbers = [x ** 2 for x in range(10)]

    squared_numbers = []
    for i in range(10):
        squared_numbers.append(i ** 2)

    squares = []
    i = 0
    while i < 10:
        i += 1
        squares.append(i ** 2)


    print(squares)

    def square(x):
        return x ** 2

    squares = [ square(x) for x in range(100) ] 

## Create a function that receives a list, and for each element 
# prints the index and the element, using enumerate

def print_index_and_element(ls):
    for count, value in enumerate(ls):
        print(f"num: {count}, value: {value}")


def print_dict(dct):
    for key, value in dct.items():
        print(f"key: {key}, value: {value}")


def test_dict():
    dct = { 1: "One", 2: "two", 3: "Three" }
    print_dict(dct)

## Create a function that receives 2 lists and returns 1 list with only 
# the elements that exist in both lists

# using copy
def exrc(ls1, ls2):
    copy = ls1.copy()
    for element in ls1:
        if not element in ls2:
            copy.remove(element)
    return copy


# using list comprehension
def exrc_comprehension(ls1, ls2):
    new_list = [x for x in ls1 if x in ls2]
    return new_list


def test_elements_in_both_lists():
    ls1 = [ "Jerusalem", "Tel-Aviv", "Haifa", "Raanana", "Kfar Sava" ]
    ls2 = [ "Haifa", "Kfar Sava" ]
    print(exrc(ls1, ls2))
    print(exrc_comprehension(ls1, ls2))
    

## Create a function that receives a list and does a left rotation using slicing
def rotate_left(ls):
     return ls[1:] + ls[:1]

def test_rotate():
    origin = [1, 2, 3, 4]
    print("Origin id: ", id(origin))
    rotated = rotate_left(origin)
    print(rotated)
    print("Rotated id: ", id(rotated))


if __name__ == "__main__":
    test_squared_numbers()
    print_index_and_element([1, 2, 3, "four"])
    test_dict()
    test_elements_in_both_lists()
    test_rotate()