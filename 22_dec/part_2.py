import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from collections import defaultdict, deque
from multiprocessing import Pool
from part_1 import (
    get_input,
    iterate
)

def get_nums(num):
    diff, res_map = deque(maxlen=4), {}
    for _ in range(2000):
        new = iterate(num)
        diff.append((new % 10) - (num % 10))
        if tuple(diff) not in res_map:
            res_map[tuple(diff)] = new % 10
        num = new
    return res_map

@timed
def main():
    data = get_input('./input.txt')
    with Pool(10) as pool:
        results = pool.map(get_nums, data)

    key_map = defaultdict(list)
    for res in results:
        for seq, value in res.items():
            if len(seq) == 4:
                key_map[seq].append(value)
    bananas = map(lambda s: sum(key_map[s]), key_map)
    print(max(bananas))

if __name__ == "__main__":
    main()
