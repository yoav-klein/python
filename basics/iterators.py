

# ---- demonstrate the use of iterators -----

numbers = [1, 2, 4, 5, 6, 3]
iter_num = iter(numbers)

print(iter_num.__next__())
print(iter_num.__next__())
# equivalent to
print(next(iter_num))

# --------- making an iterable class ---------

class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

data = [1, 2, 3, 4, 5, 6]
rev = Reverse(data)

for item in rev:
    print(item)
