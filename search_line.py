
import re
import fileinput

f = fileinput.input('.gitignore')
for line in f:
    print(line)
    if re.search("# C extensions", line):
         print("------------------")
         break;
           
 