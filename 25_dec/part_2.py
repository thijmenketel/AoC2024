import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import (
    get_input
)

@timed
def main():
    data = get_input('./test_input.txt')

if __name__ == "__main__":
    main()
