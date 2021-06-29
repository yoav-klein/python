
# Create a list containing all squared numbers between 0 - 100
# squared_numbers = [x ** 2 for x in range(100)]

squared_numbers = []
for i in range(100):
    squares.append(i ** 2)

squares = []
i = 0
while i < 100:
    i+=1
    squares.append(i ** 2)


print(squares)

def square(x):
    return x ** 2

squares = [ square(x) for x in range(100) ] 