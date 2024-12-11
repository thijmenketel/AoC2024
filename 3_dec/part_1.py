import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
import re

def get_input_as_string(filename):
    with open(filename, 'r') as file:
        return file.read()

def get_all_matching_substrings(string):
    pattern = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
    return pattern.findall(string)

@timed
def main():
    reports = get_input_as_string('./input.txt')
    print(sum(map(mul.multiply, map(eval, get_all_matching_substrings(reports)))))

class mul(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def multiply(self):
        return self.first * self.second

if __name__ == "__main__":
    main()