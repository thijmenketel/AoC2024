from http.client import FOUND
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import (
    get_input,
    find_trail_heads
)

@timed
def main():
    grid = get_input('./input.txt')
    print(sum(map(lambda heads: len(heads), find_trail_heads(grid))))

if __name__ == "__main__":
    main()
