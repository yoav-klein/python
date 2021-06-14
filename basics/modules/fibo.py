# fibonacci module

def fibonacci(num):
    a, b = 0, 1
    while a < num:
        print(a, end = ' ')
        a, b = b, a + b
    print()

def fibonacci2(num):
    a, b = 0, 1
    result = []
    while a < num:
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    import sys
    fibonacci(int(sys.argv[1]))