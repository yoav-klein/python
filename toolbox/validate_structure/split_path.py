
import os.path
import re

def search_files_rec(current_dir, path_pattern):
    first_part_in_path_pattern = path_pattern.split("/", 1)[0]
    files_found = []
    if len(path_pattern.split("/")) > 1:
        matching_subdirs = [dir for dir in os.listdir(current_dir) \
            if os.path.isdir(os.path.join(current_dir, dir)) \
            and re.search(first_part_in_path_pattern, dir)] 
        
        rest_of_path_pattern = path_pattern.split("/", 1)[1]
        for subdir in matching_subdirs:
            files_found += search_files_rec(os.path.join(current_dir, subdir), rest_of_path_pattern)
            
        return files_found

    else:
        files = [os.path.join(current_dir, file) for file in os.listdir(current_dir) \
            if re.search(first_part_in_path_pattern, file) \
            and os.path.isfile(os.path.join(current_dir, file))]

        return files


def get_files(path):
    files = search_files_rec(".", path)
    return files

print(get_files('design/m_.+/.+_init.m'))
#res = search_pattern('design/m_.+/.+_init.m', 'somepattern')
#print(f"res: {res}")
