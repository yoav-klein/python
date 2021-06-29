

import argparse

os = "linux"
parser = argparse.ArgumentParser(description="create a new repository")

parser.add_argument("repo_name", help="The name of the new repository")
if(os == "linux"):
    parser.add_argument("token", help="In linux, enter an Access Token")
args = parser.parse_args()

print(args.repo_name)
