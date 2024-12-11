import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import get_input_as_int

@timed
def main():
    left, right = get_input_as_int('./input.txt')
    total_score = sum([l * right.count(l) for l in left])

    print(total_score)

if __name__ == "__main__":
    main()