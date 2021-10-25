
# Validate Structure
---

This script is used to validate some rules against a given directory.
The user provides a JSON file in which he specifies the desired rules to be imposed.

The script reads this file and validates that the directory fulfills all the specified rules.


## Usage

### Rules file
The file is a JSON file, composed of key value dictionary. The key denotes the type of rule. Currently supported types are:
- `dir` - check that the directory exists.
- `file` - check that the file exists
- `pattern` - check that a Regex is matched in a file

You can combine rules using AND or OR:
- `and` - list of rules that must all be fulfilled
- `or` - list of rules of which one must be fulfilled

See the sample `rules.json`

### Path patterns
The paths given in the rules are matched as regular expressions. Meaning that for example:

The path `fo.+/ba.+/file.txt`

will match:
- foo/bar/file.txt
- fog/baz/file.txt
- forenzic/barbara/file.txt12


### Run

```
$ py validate_structure -f rules.json -d .
```