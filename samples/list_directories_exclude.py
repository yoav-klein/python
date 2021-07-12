

## Sometimes you want to traverse over a tree of directories, excluding some directory
import os
import re

# This uses comprehension list to create a list of tuples (root, directories, files) 
# excluding any directory containing ".git"
dirs = [ dir for dir in os.walk(".") if not re.search('.git', dir[0]) ]
print(dirs)

