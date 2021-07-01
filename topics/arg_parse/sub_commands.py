
import argparse

def commit(args):
    print(f"Commit message: {args.message}")

def push(args):
    print(f"pushing to remote {args.remote} branch {args.branch}")

# create the parser object
parser = argparse.ArgumentParser(description="git")
subparsers = parser.add_subparsers(dest='command')

push_parser = subparsers.add_parser('push', help="push to remote repository")
push_parser.add_argument('remote', help="which remote")
push_parser.add_argument('branch', help="which branch")
push_parser.set_defaults(func=push)

commit_parser = subparsers.add_parser('commit', help="commit changes")
commit_parser.add_argument('message', help="message")
commit_parser.set_defaults(func=commit)

args = parser.parse_args()

# print("You can retrieve the selected command by defining the dest argument")
# print(args.command)

args.func(args)






