
"""
This script demonstrtes the use of optional arguments
"""

import argparse

"""
Optional argument - the most simple form

We have the --verbosity argument, which is optional. If you give it a value
$ py optional_arguments.py --verbosity 1
verbose is one

  it will be set to 1
  
But you can also run it without this argument
$ py optional_arguments.py 
verbose is off
 
Note that you can't just run
$ py optional_arguments.py --verbosity 
ERROR


Uncomment the below code to experience
"""
# parser = argparse.ArgumentParser(description="optional arguments in action")
# parser.add_argument('--verbosity', help='increase verbositry')
# args = parser.parse_args()

# if(args.verbosity):
#     print("verbose is on")
# else:
#     print("verbose is off")


""" 
Use optional argument as a flag

Now the verbosity acts as a flag - just true or false
$ py optional_arguments.py --verbosity
verbose is one
  
$ py optional_arguments.py 
verbose is off
"""

# parser = argparse.ArgumentParser(description="optional arguments in action")
# parser.add_argument('--verbosity', help='increase verbositry', action='store_true')
# args = parser.parse_args()

# if(args.verbosity):
#     print("verbose is on")
# else:
#     print("verbose is off")

"""
Mutual exclusion

Let's say we have a script that should take either -minor or -major

"""

parser = argparse.ArgumentParser(description="optional arguments in action")
group = parser.add_mutually_exclusive_group(required=True) # one of them is required, either major or minor
group.add_argument('--minor', action='store_true', help='if you want to increment minor')
group.add_argument('--major', action='store_true', help='if you want to increment major')
parser.add_argument('filename', help='the file to read and write the version from and to')
args = parser.parse_args()

if(args.minor):
    print(f'incrementing minor in {args.filename}')
if(args.major):
    print(f'incrementing major in {args.filename}')