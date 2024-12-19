import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from part_1 import (
    get_input
)

def can_make_towel(towel, stripes, cache):
    if towel in cache: return cache[towel]
    result = 0
    for stripe in stripes:
        if not towel.startswith(stripe): continue
        next = towel[len(stripe):]
        if not next: 
            result += 1
            continue
        result += can_make_towel(next, stripes, cache)
    cache[towel] = result
    return result

@timed
def main():
    stripes, towels = get_input('./input.txt')
    cache = {}
    num = filter(lambda x:x != 0, map(lambda towel: can_make_towel(towel, stripes, cache), towels))
    print(sum(num))

if __name__ == "__main__":
    main()
