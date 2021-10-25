"""
validate_structure.py

A script to validate a structure of a directory, given a JSON file that describes
the desired structure to be imposed.

Usage:
$ py validate_structure.py -f/--rules-file <path_to_file> -d/--directory <path_to_directory>

"""

import re
import json
import os.path
import argparse
import logging

def _search_files_rec(current_dir, path_pattern):
    """
    takes a directory <current_dir> and a path_pattern regex and returns
    all the files matching that regex.

    example: 
    the path_pattern 'fo.+/ba.+/prog.c' will match:
        foo/bar/prog.c
        fog/baz/prog.c

    path_pattern must be a path-like string, delimited by ONLY '/' - not '\' 
    since \ also denotes a special character in regex so we can't know which is for dividing path parts and which
    is for regex special character.
    """

    first_part_in_path_pattern = path_pattern.split("/", 1)[0]
    files_found = []
    if len(path_pattern.split("/")) > 1: # if we have at least one '/'  we search for directories
        # get a list of matching subdirectories in the current directory
        matching_subdirs = [dir for dir in os.listdir(current_dir) \
            if os.path.isdir(os.path.join(current_dir, dir)) \
            and re.search(first_part_in_path_pattern, dir)]
        
        rest_of_path_pattern = path_pattern.split("/", 1)[1]
        for subdir in matching_subdirs:
            files_found += _search_files_rec(os.path.join(current_dir, subdir), rest_of_path_pattern) # add the returned files to the list of files found

        return files_found

    else:
        files_found = [os.path.join(current_dir, file) for file in os.listdir(current_dir) \
            if re.search(first_part_in_path_pattern, file) \
            and os.path.isfile(os.path.join(current_dir, file))]

        return files_found

def _get_files_by_regex(path_pattern, base_dir):
    files = _search_files_rec(base_dir, path_pattern)
    return files

class StructValidateException(Exception):
    pass

class Pattern:
    def __init__(self, path_pattern, search_pattern):
        self._path_pattern = path_pattern
        self._search_pattern = search_pattern
        logging.debug('Pattern: path: %s, search_pattern: %s', path_pattern, search_pattern)
    
    def validate(self):
        search_pattern = re.compile(self._search_pattern)
        
        matching_files_list = _get_files_by_regex(self._path_pattern, base_dir)
        logging.debug('validating Pattern: path_pattern: %s, search_pattern: %s, found files: %s', 
        self._path_pattern, self._search_pattern, matching_files_list)

        if not matching_files_list:
            logging.error('Pattern search: No files matching path_pattern: %s', self._path_pattern)
            return False
        
        for file in matching_files_list:
            found_in_file = False
            try: 
                with open(file) as f:
                    for line in f:
                        if search_pattern.search(line):
                            found_in_file = True
            except FileNotFoundError:
                raise StructValidateException('Rule pattern: File %s not found !' % file)

            if found_in_file == False:
                logging.error('Pattern search: Couldn\'t find %s in %s', self._search_pattern, self._path_pattern)
                return False

        return True

class And:
    def __init__(self, rules_list):
        self._rules_list = rules_list
    
    def validate(self):
        for rule in self._rules_list:
            if not decode(rule).validate():
                return False
        
        return True

class Or:
    def __init__(self, rules_list):
        self._rules_list = rules_list
    
    def validate(self):
        for rule in self._rules_list:
            if decode(rule).validate():
                return True
        
        return False

class DirectoryExists:
    def __init__(self, dir_path_pattern):
        self._dir_path_pattern = dir_path_pattern
    
    def validate(self):
        return os.path.isdir(self._dir_path)

class FileExists:
    def __init__(self, file_path_pattern):
        self._file_path_pattern = file_path_pattern
    
    def validate(self):
        return os.path.isfile(self._file_path)


def decode(object):
    """
    takes a dictionary object with only 1 key-value, and determines the type of
    rule by the key string. 
    instantiates a corresponding class and passes the data to its ctor.
    """
    key = list(object.keys())[0]
    value = object[key]
    if key == "and":
        return And(value) # list
    if key == "or":
        return Or(value) # list
    if key == "dir":
        return DirectoryExists(value['path'])
    if key == "file":
        return FileExists(value['path'])
    if key == "pattern":
        return Pattern(value['path'], value['pattern'])
    else:
        raise StructValidateException(f"Unknown rule type: {key}")

def main():
    try:
        with open(args.rules_file) as f:
            data = json.load(f)
    except FileNotFoundError:
        log("rules.json file not found !")
        exit(1)
    except json.decoder.JSONDecodeError:
        log("Invalid json!")
        exit(1)
    
    try:
        rules = decode(data)
        is_valid = rules.validate()
    except StructValidateException as e:
        log(e.__str__())
        exit(1)

    print(is_valid)
    

def configure_logger(loglevel):
    log_level_numeric_value = getattr(logging, loglevel.upper(), None)
    if not isinstance(log_level_numeric_value, int):
        print("Invalid log level: %s" % loglevel)
        raise ValueError('Invalid log level: %s' % loglevel)
    
    logging.basicConfig(level=log_level_numeric_value, format="%(levelname)s %(message)s")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Validate a directory structure")
    parser.add_argument("-f", "--rules-file", required=True, help="Path to json rules file")
    parser.add_argument("-d", "--directory", required=True, help="The directory to validate")
    parser.add_argument('--loglevel', help="Set the loglevel: debug, info, warning, error",
                        default="warning")
    
    args = parser.parse_args()

    return args



if __name__ == "__main__":
    args = parse_arguments()
    base_dir = args.directory # global
    if not os.path.isdir(base_dir):
        raise FileNotFoundError('Base directory not found !')
    configure_logger(args.loglevel)
    logging.info('Base directory: %s', base_dir)
    main()

    
    