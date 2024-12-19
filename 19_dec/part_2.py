import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from functools import cache
from part_1 import (
    get_input
)

@cache
def can_make_towel(towel, stripes):
    result = 0
    for stripe in stripes:
        if not towel.startswith(stripe): continue
        next = towel[len(stripe):]
        if not next: 
            result += 1
            continue
        result += can_make_towel(next, stripes)
    return result

@timed
def main():
    stripes, towels = get_input('./input.txt')
    num = filter(lambda x:x != 0, map(lambda towel: can_make_towel(towel, stripes), towels))
    print(sum(num))

if __name__ == "__main__":
    main()
