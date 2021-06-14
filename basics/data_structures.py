
print("----------------- Lists ----------------")

my_list = []
my_list.append(3)
my_list[len(my_list):] = [5, 6, 10]

# remove item
my_list.remove(6)

# remove item at specified position and return it
print(my_list.pop(1))
print(my_list)

# remove the last item
print(my_list.pop())
print(my_list)

# remove all items
my_list.clear()

my_list = [ "benny", "gadi", "danny", "yoel" ]
print("danny is in the %d place" % my_list.index("danny"))

print("there are %d dannys here" % my_list.count("danny"))

my_list.insert(1, "steven")
print(my_list)

print("---- map() -----------")

# simple example - one iterable
def mult_by_two(x):
    return x * 2

numbers = [2, 5, 12, 3]

doubles = map(mult_by_two, numbers)
print(list(doubles))

# two iterables
first_list = [1, 3, 6, 10]
second_list = [4, 10, 12, 11]

print(list(map(lambda x, y: x + y, first_list, second_list)))

print("----------- comprehension lists -------------")
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

# with no map
squares2 = [x ** 2 for x in range(5)]
print(squares2)

# multiple lists - create a list consisting of pairs of items from two lists
# if they're not the same

combs = [(x, y) for x in [1, 2, 3] for y in [4, 1, 2] if x != y]
print(combs)

print("---------- the del statement --------------")
fruit = ["apple", "watermelon", "banana", "melon","orange", "kiwi"]
del fruit[1]
print(fruit)

del fruit[2:4]
print(fruit)


print("---------------- tuples ----------------")
t = 123, 234, 'apple'
print(t)

# this will fail: tuples are immutable
# t[1] = 33

# tuples may be nested
u = t, (12, 43, 6)
print(u)

# tuple with a list
tl = ([1, 2, 3], 'mickey', 'mouse')
print(tl)
tl[0].append(4)
print(tl)

print("---------------- dictionaries ------------")

telephones = {
    'yoav': 505,
    'john': 1100,
    'alex': 9010,
}

telephones['eli'] = 999
print(telephones)
del telephones['yoav']
print(telephones)

# get a list of keys
members = list(telephones)
print(members)

# search for a key
print('eli' in telephones)

# using items() method
for member, phone in telephones.items():
    print("The phone of %s is %d" % (member, phone))