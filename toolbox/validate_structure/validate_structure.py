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
    print(f"Path pattern: {path_pattern}")
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
                    entry_found[1][:0] = list(match.groups()) # add groups captured in this match to each tuple in the list
                    entries_found.append(entry_found)
        
        return entries_found

    else:
        for entry in os.listdir(current_dir):
            match = first_part_in_path_pattern_re.search(entry)
            if match:
                entries_found.append((os.path.join(current_dir, entry), list(match.groups())))
                
        return entries_found


def _get_files_by_regex(path_pattern):
    matching_entries = _search_entries_regex_rec(base_dir, path_pattern)
    files = [entry for entry in matching_entries if os.path.isfile(entry[0])]
    return files

def _get_directories_by_regex(path_pattern):
    matching_entries = _search_entries_regex_rec(base_dir, path_pattern)
    dirs = [entry for entry in matching_entries if os.path.isdir(entry[0])]
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
            if not Pattern._search_pattern_in_file(file[0], search_pattern):
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

class Directory:
    """
    validates a directory (or a set of directories). takes a regex to match a path, and optionally
    other fields used to validate the directory(ies). those fields are validated using the corresponding
    subclasses.
    """

    class Files:
        """
        validates existence of files in the directories
        """
        def __init__(self, files_list):
            self._files_list = files_list
        
        def validate(self, directories):
            for directory in directories:
                if not Directory.Files._search_files_in_dir(directory, self._files_list):
                    return False
                
            return True

        def _search_files_in_dir(directory, files_list):
            logging.debug(f'Directory::_search_files_in_dir: Directory: {directory}')
            for file in files_list:
                logging.debug(f'Directory::_search_files_in_dir: File {file}')
                for i in range(len(directory[1])): # directory is a tuple ('directory_path', [groups])
                    file = file.replace(f'\{str(i)}', directory[1][i])
                logging.debug(f'Directory::_search_files_in_dir: Aftr replace: {file}')
                file_to_search = os.path.join(directory[0], file)   
                if not os.path.isfile(file_to_search):
                    logging.warning(f'did not find {file_to_search}')
                    return False
            
            return True
    
    class OnlyFolders:
        """
        validates that the directories contain only folders, no files
        """
        def __init__(self):
            pass
        
        def validate(self, directories):
            for directory in directories:
                files_list = [entry for entry in os.listdir(directory[0]) if os.path.isfile(os.path.join(directory[0], entry))]
                if len(files_list):
                    logging.warning(f'OnlyFolders::validate: Found files in {directory[0]}')
                    return False
            
            return True

        
    def __init__(self, data):
        self._data = data
        self._validation_list = []
        if 'files' in self._data:
            self._validation_list.append(Directory.Files(self._data['files']))
        if 'only_folders' in self._data and self._data['only_folders'] == True:     
            self._validation_list.append(Directory.OnlyFolders())

    def validate(self):
        found_dirs = _get_directories_by_regex(self._data['path'])
        logging.debug("Directory::validate: pattern: %s, Found: %s", self._data['path'], found_dirs)
        
        if len(found_dirs) == 0:
            logging.warning("Directory wasn't found: %s", self._data['path'])
            return False
        
        for validation_item in self._validation_list:
            if not validation_item.validate(found_dirs):
                return False
        
        return True

class File:
    """
    validates the existence of a file
    """
    def __init__(self, data):
        self._data = data
    
    def validate(self):
        files_found = _get_files_by_regex(self._data['path'])
        logging.debug("File: %s, Found: %s", self._data['path'], files_found)
        
        if len(files_found) == 0:
            logging.warning("File wasn't found: %s", self._data['path'])
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
        return Directory(value)
    if key == "file":
        return File(value)
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
