
import sys
from .calculator import add

def main():
    print(add(int(sys.argv[1]), int(sys.argv[2])))