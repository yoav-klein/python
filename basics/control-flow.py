

print("------------- While --------------")
a, b = 0, 1
while a < 1000:
    print(a, end=",")
    a, b = b, a + b

a = 0
while a < 10:
    a = a + 1
    print(a)

print("------------- If ------------")
num = int(input("please enter a number: "))
if num == 0:
    print("Zero?")
elif num > 0:
    print("Positive today")
else:
    print("Not zero, not positive, you must be negative")


print("-------------- For --------------")

list = [ "cat", "window", "car" ]
for item in list:
    print(item, len(item))


boys = [ "tommy", "billy", "moti" ]
for boy in boys:
    if(boy == "billy"):
        boy = "bolly"
    print(boy)
