
import os.path
import re


def search_rec(current_dir, path_pattern, search_pattern):
    first_part_in_path_pattern = path_pattern.split("/", 1)[0]
    
    if len(path_pattern.split("/")) > 1:
        matching_subdirs = [dir for dir in os.listdir(current_dir) \
            if os.path.isdir(os.path.join(current_dir, dir)) \
            and re.search(first_part_in_path_pattern, dir)] 
        
        sum = 0
        rest_of_path_pattern = path_pattern.split("/", 1)[1]
        for subdir in matching_subdirs:
            result = search_rec(os.path.join(current_dir, subdir), rest_of_path_pattern, search_pattern)
            if -1 == result:
                return -1
            sum += result
        
        return sum

    else:
        files = [file for file in os.listdir(current_dir) \
            if re.search(first_part_in_path_pattern, file) \
            and os.path.isfile(os.path.join(current_dir, file))]

        sum = 0
        for file in files:
            found = False
            print(f"Searching in {os.path.join(current_dir, file)}")
            with open(os.path.join(current_dir, file)) as f:
                for line in f:
                    if re.search(search_pattern, line):
                        found = True
                        sum += 1
            if found == False:
                print(f"Didn't find {search_pattern} in {os.path.join(current_dir, file)}")
                return -1

        return sum

def search_pattern(path, pattern):
    result = search_rec(".", path, pattern)
    return result
    

res = search_pattern('design/m_.+/.+_init.m', 'somepattern')
print(f"res: {res}")
