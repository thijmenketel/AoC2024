import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
import re
from part_1 import get_input_as_string, mul

def get_all_matching_substrings(string):
    pattern = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)")
    return pattern.findall(string)

def filter_matches(matches):
    dont = False
    for entry in matches:
        if entry == "do()":
            dont = False
        elif entry == "don't()":
            dont = True
        elif not dont:
            yield entry
    
@timed
def main():
    input_string = get_input_as_string('./input.txt')
    cleaned = filter_matches(get_all_matching_substrings(input_string))

    print(sum(map(mul.multiply, map(eval, cleaned))))

if __name__ == "__main__":
    main()