
# formatted string literals
event = "Mondial"
year = "2022"
print(f'Who will win the {event} in {year} ?')

# using fomrat specifier
import math
print(f'The value of pi is around {math.pi:.3f}')

table = { 'yoshiahu': 21, 'dan': 20, 'yoel': 50 }
for name, grade in table.items():
    print(f'{name:10} ===> {grade:4}')


# str.format()

print('Hello mr. {}, today is {}. Is it a good day?'.format("Yoav", "tuesday"))
print('Hello {1}, Today is {0}', "Thursday", "Yoav")
print('This {food} is {adjective}'.format(food="Spaghetti", adjective="Terrible"))


# file operations
with open("log.txt", 'w') as logger:
    logger.write("Starting program")

# verify the file is closed
print(logger.closed)

with open("poem.txt", 'r') as poem_file:
    line = poem_file.readline()
    poem = poem_file.read()

print(f"First line is {line}")
print("And the rest of the poem is:")

with open("poem.txt", 'r') as poem_file:
    for line in poem_file:
        print(line, end = '')

# converting dictionary to string in order to write it
s = str(table)
with open("phones.txt", "w") as phones:
    phones.write(s)

# working with json

import json
with open('phones.json', 'w') as phone_json:
    json.dump(table, phone_json)


### repr

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"My name is {self.name} and I'm {self.age} years old"

yoav = Person("Yoav", 34)
print(repr(yoav))
