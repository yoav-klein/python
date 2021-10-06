
# Validate Structure
---

This script is used to validate some rules against a given directory.
The user provides a JSON file in which he specifies the desired rules to be imposed.

The script reads this file and validates that the directory fulfills all the specified rules.


## Usage

### Rules file
The file is a JSON file, composed of key value dictionary. The key denotes the type of rule. Currently supported types are:
- `dir` - check that the directory exists
- `file` - check that the file exists
- `and` - list of rules that must all be fulfilled
- `or` - list of rules of which one must be fulfilled
- `pattern` - check that a Regex is matched in a file

See the sample `rules.json`

### Run

```
$ py validate_structure -f rules.json -d .
```