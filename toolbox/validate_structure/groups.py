
import re

# s = "foo"


# m = re.search("f(o)o(.*)", s)

# print(m)
# print(dir(m))
# print(m.groups())

#lst = [(1,2), (3,4)]

#tup = ("file.txt", [1, 2, 3])
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# lst1[0:0] = lst2
# print(lst1)

#lst += tuple(1, 2)
#lst += [(3, 4)]


# class FileSystemContext:
#     def __init__(self, path, groups):
#         self.path = path
#         self.groups = groups


# fsc = FileSystemContext("foo/bar/file.txt", ["o", "b"])

# print(fsc.path)

obj = {
    "one": 1,
    "two": 2
}

obj2 = dict(obj)
print(obj2 is obj)