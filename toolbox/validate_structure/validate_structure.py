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
                matching_entries_in_dir = _search_entries_regex_rec(os.path.join(current_dir, subdir), rest_of_path_pattern)
                for matching_entry in matching_entries_in_dir:
                    matching_entry[1][:0] = list(match.groups()) # add groups captured in this match to each tuple in the list
                    entries_found.append(matching_entry)
        
        return entries_found

    else:
        for entry in os.listdir(current_dir):
            match = first_part_in_path_pattern_re.search(entry)
            if match:
                entries_found.append((os.path.join(current_dir, entry), list(match.groups())))
                
        return entries_found


def _get_files_by_regex(path_pattern):
    matching_entries = _search_entries_regex_rec(base_dir, path_pattern)
    print(matching_entries)
    files = [file for file, groups in matching_entries if os.path.isfile(file)]
    return files

def _get_directories_by_regex(path_pattern):
    matching_entries = _search_entries_regex_rec(base_dir, path_pattern)
    dirs = [file for file, groups in matching_entries if os.path.isdir(file)]
    return dirs

class StructValidateException(Exception):
    pass

class Pattern:
    def __init__(self, path_pattern, search_pattern):
        self._path_pattern = path_pattern
        self._search_pattern = search_pattern
    
    def _search_pattern_in_file(file, pattern):
        try: 
            with open(file) as f:
                for line in f:
                    if pattern.search(line):
                        return True
        except FileNotFoundError:
            raise StructValidateException('Rule pattern: File %s not found !' % file)
        
        return False

    def validate(self):
        search_pattern = re.compile(self._search_pattern)
        
        matching_files_list = _get_files_by_regex(self._path_pattern)
        logging.debug('Pattern: path_pattern: %s, search_pattern: %s, found files: %s', 
        self._path_pattern, self._search_pattern, matching_files_list)

        if not matching_files_list:
            logging.warning('Pattern search: No files matching path_pattern: %s', self._path_pattern)
            return False
        
        for file in matching_files_list:
            if not Pattern._search_pattern_in_file(file, search_pattern):
                logging.warning('Pattern search: Couldn\'t find %s in %s', self._search_pattern, self._path_pattern)
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
        dirs = _get_directories_by_regex(self._dir_path_pattern)
        logging.debug("Directory: %s, Found: %s", self._dir_path_pattern, dirs)
        
        if len(dirs) == 0:
            logging.warning("Directory wasn't found: %s", self._dir_path_pattern)
            return False
        
        return True

class FileExists:
    def __init__(self, file_path_pattern):
        self._file_path_pattern = file_path_pattern
    
    def validate(self):
        files = _get_files_by_regex(self._file_path_pattern)
        logging.debug("File: %s, Found: %s", self._file_path_pattern, files)
        
        if len(files) == 0:
            logging.warning("File wasn't found: %s", self._file_path_pattern)
            return False
        
        return True


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
        rules = decode(data)
        is_valid = rules.validate()
    except StructValidateException as e:
        log(e.__str__())
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
