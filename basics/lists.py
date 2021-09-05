
## slicing creates a new object
squares = [1, 4, 9, 25, 36]

print("squares: ")
print(squares)
print("squares id:")
print(id(squares))

new = squares[0:2]
print("new: ")
print(new)
print("new id:")
print(id(new))

## concatenating lists
print("Concatenate:")
print(squares + [49, 64, 81, 100])

## appending
squares.append(49)
print("Appended 49")
print(squares)

## assigning to slices
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# replace some values
letters[2:5] = ['C', 'D', 'E']
print("New values of letters: ")
print(letters)

# now remove them
letters[2:5] = []
print("Now removing them")
print(letters)

## length of a list
print(len(letters))

## Nesting lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print("x[0]:", x[0])
print("x[0][1]:", x[0][1])
