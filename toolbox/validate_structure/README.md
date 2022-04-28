
# Validate Structure
---

This script is used to validate some rules against a given directory.
The user provides a JSON file in which he specifies the desired rules to be imposed.

The script reads this file and validates that the directory fulfills all the specified rules.


## Usage

### Rules file
The user provides a JSON file which specifies the rules he likes to impose. Rules may be imposed to either a `file` or a directory (`dir`). Rules may be combined using `or` and `and`.

The rules file should contain an object with one field specifying either:
- `file`
- `dir`
- `and`
- `or`

IMPORTANT: all paths must include '/', not '\', even if you're on Windows.

#### file
The `file` type must include the following fields:
- `path` - a regex specifying the path of the file
- `mandatory` - whether or not at least one file must be found.

It may include a `rules` field, in which he can specify rules that the matching directory(ies) must follow. Supported rules for files are:
- `pattern`: A regex that must be matched in the file.
- `matching_file`: A file that must exist in the same directory as this file.


#### dir
The `dir` type must include the following fields:
- `path` - a regex specifying the path of the directory
- `mandatory` - whether or not at least one directory must be found.

It may include a `rules` field, in which he can specify rules that the matching directory(ies) must follow.
Supported rules for directories are:
- `file` - the above file object -  check for a file in the directory. In this case, the `path` of the file is relative to the base of the directories found.
- `only_folders` - boolean - whether or not the directory must include only folders. 

See the sample `rules.json`

### Path patterns
The paths given in the rules are matched as regular expressions. Meaning that for example:

The path `fo.+/ba.+/file.txt`

will match:
- foo/bar/file.txt
- fog/baz/file.txt
- forenzic/barbara/file.txt12

In this case, all the found files will be examined against the `rules` field of that `file` object.

### Run

```
$ py validate_structure -f rules.json -d .
```