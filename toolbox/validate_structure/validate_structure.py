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

class StructValidateException(Exception):
    pass

class Pattern:
    def __init__(self, file_path, pattern):
        self._file_path = file_path
        self._pattern = pattern
    
    def validate(self):
        pattern = re.compile(self._pattern)
        
        try:
            with open(self._file_path) as f:
                for line in f:
                    if pattern.search(line):
                        return True
        except FileNotFoundError:
            raise StructValidateException(f"Rule pattern: File {self._file_path} not found !")

        return False

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
    def __init__(self, dir_path):
        self._dir_path = dir_path
    
    def validate(self):
        return os.path.isdir(self._dir_path)

class FileExists:
    def __init__(self, file_path):
        self._file_path = file_path
    
    def validate(self):
        return os.path.isfile(self._file_path)

base_dir = ''


def log(message):
    print("Error: " + message)

def construct_path(path):
    """
    construct a path from the base_dir and the received path
    """
    return os.path.join(base_dir, path)

def decode(object):
    """
    takes a dictionary object with only 1 key-value, and determines the type of
    rule by the key string. 
    instantiates a corresponding class and passes the data to its ctor.
    """
    key = list(object.keys())[0]
    value = object[key]
    if key == "dir":
        return DirectoryExists(construct_path(value['path']))
    if key == "file":
        return FileExists(construct_path(value['path']))
    if key == "and":
        return And(value) # list
    if key == "or":
        return Or(value) # list
    if key == "pattern":
        return Pattern(construct_path(value['path']), value['pattern'])
    else:
        raise StructValidateException(f"Unknown rule type: {key}")


def main():
    parser = argparse.ArgumentParser(description="Validate a directory structure")
    parser.add_argument("-f", "--rules-file", required=True, help="Path to json rules file")
    parser.add_argument("-d", "--directory", required=True, help="The directory to validate")
    
    args = parser.parse_args()
    global base_dir
    base_dir = args.directory

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

if __name__ == "__main__":
    main()

    
    