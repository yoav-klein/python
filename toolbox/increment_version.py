
"""
increment_version.py - increment a semver based on git history

This script reads the tags of the git repository, and according to user's choice, 
increments the major/minor version, and outputs the result to stdout

parameters:
- major/minor

$ py increment_version.py -major
$ py increment_version.py -minor

"""
import subprocess
import argparse

def run_git(command):
    try:
        process = subprocess.run(['git'] + command, check=True, capture_output=True)
        return process
    except subprocess.SubprocessError as err:
        print("Git encountered some error")
        print(process.stderr.decode())
        raise err
    except OSError as err:
        print("You probably don't have git in path")
        print(err)
        raise err


def inc_major(latest):
    if not latest:
        return '1.0'
    
    major, minor = latest.split('.')
    return f'{int(major)+1}.0'

def inc_minor(latest):
    if not latest:
        return '0.1'
    
    major, minor = latest.split('.')
    return f'{major}.{int(minor)+1}'


parser = argparse.ArgumentParser(description="optional arguments in action")
group = parser.add_mutually_exclusive_group(required=True) # one of them is required, either major or minor
group.add_argument('--minor', action='store_true', help='if you want to increment minor')
group.add_argument('--major', action='store_true', help='if you want to increment major')

if __name__ == "__main__":
    args = parser.parse_args()
    git_tag = run_git(['tag', '--sort=-v:refname'])
    decoded_output = git_tag.stdout.decode()
    latest, newline, rest = decoded_output.partition('\n')
    
    if(args.major):
        print(inc_major(latest))
    if(args.minor):
        print(inc_minor(latest))
