"""
validate_structure.py

A script to validate a structure of a directory, given a JSON file that describes
the desired structure to be imposed.

Usage:
$ py validate_structure.py -f/--rules-file <path_to_file> -d/--directory <path_to_directory> [--loglevel <info/debug/warning/error/critical>]
"""

import jsonschema
import re
import json
import os.path
import argparse
import logging
import copy

from typing import List
from pathlib import Path

base_dir = ''

class FileSystemContext:
    def __init__(self, path, captures):
        self.path = path
        self.captures = captures
    def __str__(self):
        return f"FileSystemContext(path={self.path}, captures={self.captures})"


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
                    entry_found.captures[:0] = list(match.groups()) # add groups captured in this match to each tuple in the list
                    entries_found.append(entry_found)
        
        return entries_found

    else:
        for entry in os.listdir(current_dir):
            match = first_part_in_path_pattern_re.search(entry)
            if match:
                entries_found.append(FileSystemContext(os.path.join(current_dir, entry), list(match.groups())))
                
        return entries_found

def validate_directory(dir_data: dict, fsctx: FileSystemContext) -> bool:
    def only_folders(directory: FileSystemContext, mandatory: bool) -> bool:
        if mandatory:
            if len([file for file in os.listdir(directory.path) if os.path.isfile(os.path.join(directory.path, file))]) > 0:
                logging.warning(f"Directory {directory.path} contains files !")
                return False
        
        return True


    def all_of(directory: FileSystemContext, rule_list: List[dict]) -> bool:
        for rule in rule_list:
            is_valid = validate(directory, rule)
            if not is_valid:
                return False
        
        return True
    
    def one_of(directory: FileSystemContext, rule_list: List[dict]) -> bool:
        for rule in rule_list:
            is_valid = validate(directory, rule)
            if is_valid:
                return True
        
        return False

    def validate(directory: FileSystemContext, rules: dict) -> bool:
        rule_type = list(rules.keys())[0]
        rule_content = rules[rule_type]
        if rule_type == "file":
            return validate_file(rule_content, directory)
        elif rule_type == "dir":
            return validate_directory(rule_content, directory)
        elif rule_type == "only_folders":
            return only_folders(directory, rule_content)
        elif rule_type == "and":
            return all_of(directory, rule_content)
        elif rule_type == "or":
            return one_of(directory, rule_content)
        else:
            raise ValueError(f"directory rule type {rule_type} is invalid !")

    logging.debug(f"Directory validation: {dir_data['path']}, context: {fsctx.path}")

    directory_path = copy.copy(dir_data['path']) # not working directly on data['path'] because it may be needed as is
                                             # in the check of other directories
    for capture_index in range(len(fsctx.captures)):
        directory_path = directory_path.replace(f'\{str(capture_index)}', fsctx.captures[capture_index])
    
    found_dirs = [entry for entry in _search_entries_regex_rec(fsctx.path, directory_path) if os.path.isdir(entry.path)]
    if dir_data['mandatory'] == True and not found_dirs:
        logging.warning(f"Directory {directory_path} not found !")
        return False

    if not 'rules' in dir_data:
        return True

    for found_dir in found_dirs:
        logging.debug(f"Directory validation {found_dir.path}, validating rules")
        found_dir.captures[0:0] = fsctx.captures
        is_valid = validate(found_dir, dir_data['rules'])
        if not is_valid:
            return False
    
    return True

def validate_file(file_data: dict, fsctx: FileSystemContext) -> bool:
    def check_size(file, size):
        """
        TODO
        """
        return True

    def check_pattern(file: FileSystemContext, pattern: str) -> bool:
        # replace tokens in pattern
        for capture_index in range(len(file.captures)):
            pattern = pattern.replace(f'\{str(capture_index)}', file.captures[capture_index])
        
        pattern_re = re.compile(pattern)
        logging.debug(f"Pattern validation: file: {file.path}, pattern: {pattern}")
        with open(file.path) as f:
            for line in f:
                if pattern_re.search(line):
                    return True
        
        logging.warning(f"Pattern: didn't find {pattern} in {file.path}")
        return False

    def all_of(file: FileSystemContext, rule_list: List[dict]) -> bool:
        for rule in rule_list:
            is_valid = validate(file, rule)
            if not is_valid:
                return False
        
        return True
    
    def one_of(file: FileSystemContext, rule_list: List[dict]) -> bool:
        for rule in rule_list:
            is_valid = validate(file, rule)
            if is_valid:
                return True
        
        return False

    def validate(file: FileSystemContext, rules: dict) -> bool:
        rule_type = list(rules.keys())[0]
        rule_content = rules[rule_type]
        if rule_type == "pattern":
            return check_pattern(file, rule_content)
        elif rule_type == "size":
            return check_size(file, rule_content)
        elif rule_type == "and":
            return all_of(file, rule_content)
        elif rule_type == "or":
            return one_of(file, rule_content)
        else:
            raise ValueError('invalid rule type')

    logging.debug(f"File validation: path: {file_data['path']}, context: {fsctx}")
    file_path = copy.copy(file_data['path'])
    for capture_index in range(len(fsctx.captures)):
        file_path = file_path.replace(f'\{str(capture_index)}', fsctx.captures[capture_index]) # turn \0 to the first item in captures, etc.

    logging.debug(f"After replacement of captures: {file_path}")
    found_files = [entry for entry in _search_entries_regex_rec(fsctx.path, file_path) if os.path.isfile(entry.path)]
    
    if file_data['mandatory'] == True and not found_files:
        logging.warning(f"file {os.path.join(fsctx.path, file_path)} not found !")
        return False
    
    logging.debug(f"Found files: {[entry.path for entry in found_files]}")
    
    if not 'rules' in file_data:
        return True
    
    for found_file in found_files:
        found_file.captures[0:0] = fsctx.captures
        logging.debug(f"File validating: {found_file.path}, {found_file.captures}")
        is_valid = validate(found_file, file_data['rules'])
        if not is_valid:
            return False
    
    return True

def all_of(data: List[dict], directory: Path) -> bool:
    for rule in data:
        is_valid = validate(directory ,rule)
        if not is_valid:
            return False
    
    return True

def one_of(data: List[dict], directory: Path) -> bool:
    for rule in data:
        is_valid = validate(directory, rule)
        if is_valid:
            return True
    
    return False

def validate(base_dir: Path, rules: dict) -> bool:
    """
    takes a dictionary 'rules' with only 1 key-value, and determines the type of
    rule by the key. 
    calls the relevant validation function and passes the data.
    """
    rule_type = list(rules.keys())[0]
    rule_content = rules[rule_type]
    if rule_type == "and":
        return all_of(rule_content, base_dir) 
    elif rule_type == "or":
        return one_of(rule_content, base_dir) 
    elif rule_type == "dir":
        return validate_directory(rule_content, FileSystemContext(base_dir, []))
    elif rule_type == "file":
        return validate_file(rule_content, FileSystemContext(base_dir, []))
    else:
        raise ValueError(f"Unknown rule type: {rule_type}")    

def configure_logger(loglevel):
    log_level_numeric_value = getattr(logging, loglevel.upper(), None)
    if not isinstance(log_level_numeric_value, int):
        print("Invalid log level: %s" % loglevel)
        raise ValueError('Invalid log level: %s' % loglevel)
    
    logging.basicConfig(level=log_level_numeric_value, format="%(levelname)s %(message)s")

def validate_structure(directory: str, rules: dict) -> bool:
    base_dir = Path(directory)
    if not base_dir.is_dir():
        raise FileNotFoundError('Base directory not found')
    
    logging.info('Base directory: %s', base_dir)

    is_valid = validate(base_dir, rules)
    
    if is_valid:
        print('Directory is valid !')
    else:
        print('Directory is invalid !!!')
    
    return is_valid

def read_data(rules_file: str, schema_file: str) -> dict:
    """
    read the rules JSON file and validate it against the schema
    """    
    def read_json_file(file_path: str) -> dict:
        try:
            with open(file_path) as f:
                return json.load(f)
                
        except FileNotFoundError:
            logging.critical(f"file {file_path} not found !")
            raise
        except json.decoder.JSONDecodeError:
            logging.critical(f"{file_path} is an invalid JSON!")
            raise


    schema = read_json_file(schema_file)
    rules = read_json_file(rules_file)
        
    try:
        jsonschema.validate(instance=rules, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        logging.error("Your rules.json file is invalid !!!")
        raise

    return rules

def parse_arguments():
    parser = argparse.ArgumentParser(description="Validate a directory structure")
    parser.add_argument("-f", "--rules-file", required=True, help="Path to json rules file")
    parser.add_argument("-d", "--directory", required=True, help="The directory to validate")
    parser.add_argument('--loglevel', help="Set the loglevel: debug, info, warning, error",
                        default="warning")
    args = parser.parse_args()

    return args





def main(args):
    configure_logger(args.loglevel)
    
    rules = read_data(args.rules_file, 'schema.json')
    is_valid = validate_structure(args.directory, rules)
    
    if not is_valid:
        exit(1)

if __name__ == "__main__":
    args = parse_arguments()
    main(args)
