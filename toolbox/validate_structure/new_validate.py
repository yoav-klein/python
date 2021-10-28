"""
validate_structure.py

A script to validate a structure of a directory, given a JSON file that describes
the desired structure to be imposed.

Usage:
$ py validate_structure.py -f/--rules-file <path_to_file> -d/--directory <path_to_directory> [--loglevel <info/debug/warning/error/critical>]
"""

import re
import json
import os.path
import argparse
import logging



class FileSystemContext:
    def __init__(self, path, groups):
        self.path = path
        self.groups = groups


def _search_entries_regex_rec(current_dir, path_pattern):
    """
    takes a directory <current_dir> and a path_pattern regex and returns
    all the file system entries matching that regex. (both directories and files)

    example: 
    the path_pattern 'fo.+/ba.+/prog.c' will match:
        foo/bar/prog.c
        fog/baz/prog.c
    the path_pattern fo.+/ba.+ will match:
        foo/bar
        fog/barbara.txt

    path_pattern must be a path-like string, delimited by ONLY '/' - not '\' 
    since \ also denotes a special character in regex so we can't know which is for dividing path parts and which
    is for regex special character.
    """
    first_part_in_path_pattern = path_pattern.split("/", 1)[0]
    first_part_in_path_pattern_re = re.compile(first_part_in_path_pattern)
    entries_found = []
    if len(path_pattern.split("/")) > 1: # if we have at least one '/'  we search for directories
        rest_of_path_pattern = path_pattern.split("/", 1)[1]
        for subdir in [entry for entry in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, entry))]:
            match = first_part_in_path_pattern_re.match(subdir)
            if match:
                entries_found_in_subdir = _search_entries_regex_rec(os.path.join(current_dir, subdir), rest_of_path_pattern)
                for entry_found in entries_found_in_subdir:
                    entry_found.groups[:0] = list(match.groups()) # add groups captured in this match to each tuple in the list
                    entries_found.append(entry_found)
        
        return entries_found

    else:
        for entry in os.listdir(current_dir):
            match = first_part_in_path_pattern_re.search(entry)
            if match:
                entries_found.append(FileSystemContext(os.path.join(current_dir, entry), list(match.groups())))
                
        return entries_found


def _get_files_by_regex(path_pattern):
    matching_entries = _search_entries_regex_rec(base_dir, path_pattern)
    files = [entry for entry in matching_entries if os.path.isfile(entry[0])]
    return files

def _get_directories_by_regex(path_pattern):
    matching_entries = _search_entries_regex_rec(base_dir, path_pattern)
    dirs = [entry for entry in matching_entries if os.path.isdir(entry[0])]
    return dirs


def validate_directory(data, fsctx):
    def check_size(file, size):
        return True

    def all_of(directory, data):
        if not isinstance(data, list):
            raise ValueError("and must be a list !")
        
        for rule in data:
            is_valid = directory.validate(data, data)
            if not is_valid:
                return False
        
        return True
    
    def one_of(directory, data):
        if not isinstance(data, list):
            raise ValueError("and must be a list !")

        for rule in data:
            is_valid = directory.validate(data, data)
            if is_valid:
                return True
        
        return False

    def validate(directory, obj):
        rule_type = obj.keys()[0]
        data = obj[rule_type]
        if rule_type == "file":
            file(data, directory)
        if rule_type == "size":
            check_size(file, data)
        if rule_type == "and":
            all_of(file, data)
        if rule_type == "or":
            one_of(file, data)

    for group_index in range(len(fsctx.groups)):
        data.path = data.path.replace(f'\{str(group_index)}', fsctx.groups[group_index])
    
    found_dirs = _get_directories_by_regex(os.path.join(fsctx.path), data.path)

    if data.mandatory == True and not found_dirs:
        return False

    for found_dir in found_dirs:
        found_dir.groups[0:0] = fsctx.groups
        validate(found_dir, data.rules)


def validate_file(data, fsctx):
    def check_size(file, size):
        return True

    def check_pattern(file, pattern):
        print(f"looking for {pattern} in {file.path}, {file.groups}")
        return True

    def all_of(file, data):
        if not isinstance(data, list):
            raise ValueError("and must be a list !")

        for rule in data:
            is_valid = file.validate(file, data)
            if not is_valid:
                return False
        
        return True
    
    def one_of(file, data):
        if not isinstance(data, list):
            raise ValueError("and must be a list !")

        for rule in data:
            is_valid = file.validate(file, data)
            if is_valid:
                return True
        
        return False

    def validate(file, obj):
        print(file)
        print(obj)
        rule_type = list(obj.keys())[0]
        data = obj[rule_type]
        if rule_type == "pattern":
            return check_pattern(file, data)
        elif rule_type == "size":
            return check_size(file, data)
        elif rule_type == "and":
            return all_of(file, data)
        elif rule_type == "or":
            return one_of(file, data)
        else:
            raise ValueError('invalid rule type')

    for group_index in range(len(fsctx.groups)):
        data.path = data.path.replace(f'\{str(group_index)}', fsctx.groups[group_index])
    
    #found_files = _get_files_by_regex()
    found_files = _search_entries_regex_rec(fsctx.path, data['path'])
    
    #print(type(found_files))
    if data['mandatory'] == True and not found_files:
        return False

    for found_file in found_files:
        found_file.groups[0:0] = fsctx.groups
        is_valid = validate(found_file, data['rules'])
        if not is_valid:
            return False
    
    return True

def all_of(data):
    if not isinstance(data, list):
        raise ValueError("and must be a list !")
    
    for rule in data:
        is_valid = validate(rule)
        if not is_valid:
            return False
    
    return True

def one_of(data):
    if not isinstance(data, list):
        raise ValueError("or must be a list !")
    
    for rule in data:
        is_valid = validate(rule)
        if is_valid:
            return True
    
    return False


def validate(object):
    """
    takes a dictionary object with only 1 key-value, and determines the type of
    rule by the key string. 
    instantiates a corresponding class and passes the data to its ctor.
    """
    rule_type = list(object.keys())[0]
    value = object[rule_type]
    if rule_type == "and":
        return all_of(value) # list
    if rule_type == "or":
        return one_of(value) # list
    if rule_type == "dir":
        return validate_directory(value, FileSystemContext(base_dir, []))
    if rule_type == "file":
        return validate_file(value, FileSystemContext(base_dir, []))
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")    


def configure_logger(loglevel):
    log_level_numeric_value = getattr(logging, loglevel.upper(), None)
    if not isinstance(log_level_numeric_value, int):
        print("Invalid log level: %s" % loglevel)
        raise ValueError('Invalid log level: %s' % loglevel)
    
    logging.basicConfig(level=log_level_numeric_value, format="%(levelname)s %(message)s")

def validate_structure(directory, rules_file, loglevel='warning'):
    configure_logger(loglevel)
    global base_dir
    base_dir = os.path.normpath(directory)
    if not os.path.isdir(base_dir):
        raise FileNotFoundError('Base directory not found')
    
    logging.info('Base directory: %s', base_dir)
    
    try:
        with open(rules_file) as f:
            data = json.load(f)
    except FileNotFoundError:
        logging.critical("rules.json file not found !")
        raise
    except json.decoder.JSONDecodeError:
        logging.critical("Invalid json!")
        raise
    
    try:
        is_valid = validate(data)
    except Exception as e:
        logging.error(e.__str__())
        raise

    if is_valid:
        logging.info('Directory is valid !')
    else:
        logging.error('Directory is invalid !')
    
    return is_valid

def parse_arguments():
    parser = argparse.ArgumentParser(description="Validate a directory structure")
    parser.add_argument("-f", "--rules-file", required=True, help="Path to json rules file")
    parser.add_argument("-d", "--directory", required=True, help="The directory to validate")
    parser.add_argument('--loglevel', help="Set the loglevel: debug, info, warning, error",
                        default="warning")
    args = parser.parse_args()

    return args

def main():
    args = parse_arguments()
    is_valid = validate_structure(args.directory, args.rules_file, args.loglevel)
    
    if not is_valid:
        exit(1)

if __name__ == "__main__":
    main()
