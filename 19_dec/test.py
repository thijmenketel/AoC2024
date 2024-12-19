import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import (
    get_input
)

def can_make_towel(towel, stripes):
    for stripe in stripes:
        sub = towel.startswith(stripe)
        if not sub: continue
        next = towel[len(stripe):]
        if not next: return True
        if can_make_towel(next, stripes):
            return True
    return False
        

@timed
def main():
    stripes, towels = get_input('./test_input.txt')
    num = filter(lambda x:x, map(lambda towel: can_make_towel(towel, stripes), towels))
    print(len(list(num)))



if __name__ == "__main__":
    main()
