
import os.path
import re

path = os.path.normpath("foo/bar/baz")
path_components = path.split(os.sep)
current = os.getcwd()

def search_rec(current_dir, path_pattern, search_pattern):
    print("-----------")
    path_pattern = os.path.normpath(path_pattern)
    path_pattern_components = path_pattern.split(os.sep)
    
    print(f"Current path: {current_dir}")
    print(f"Path pattern: {path_pattern}")
    
    current_pattern = path_pattern.split(os.sep, 1)[0]
    
    print(f"Current pattern: {current_pattern}")
    print(f"path_pattern_components: {len(path_pattern_components)}")
    
    if len(path_pattern_components) > 1:
        next_pattern = path_pattern.split(os.sep, 1)[1]
        print(f"Next pattern: {next_pattern}")
        print(f"Current dir contents: {os.listdir(current_dir)}")
        subdirs = [dir for dir in os.listdir(current_dir)] #  if re.search(current_pattern, dir) and os.path.isdir(dir)
        matching_dirs = []
        for dir in subdirs:
            search_res = re.search(current_pattern, dir)
            print(f"dir: {dir}: {re.search(current_pattern, dir)}")
            if(search_res):
                matching_dirs.append(dir)
        #print(f"Matching subdirs: {subdirs}")
        sum = 0
        for subdir in matching_dirs:
            result = search_rec(os.path.join(current_dir, subdir), next_pattern, search_pattern)
            if -1 == result:
                return -1
            sum += result
        
        return sum

    else:
        print(f"Dir contents: {os.listdir(current_dir)}")
        files = [file for file in os.listdir(current_dir) if re.search(current_pattern, file) and os.path.isfile(os.path.join(current_dir, file))]
        print(f"Found files: {files}")
        for file in files:
            print(f"Searching in {path_pattern}")
        return 0

def search_pattern(path, pattern):
    result = search_rec(".", path, pattern)
    

search_pattern('ba.+/fo.+/ben.txt', 'somepattern')