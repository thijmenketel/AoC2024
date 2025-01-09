from itertools import product
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed

def get_input(filename):
    with open(filename, 'r') as file:
        grids = [grid.split('\n') for grid in file.read().strip().split('\n\n')]
        locks, keys = [], []
        for grid in grids:
            if grid[0][0] == '#':
                locks.append(grid)
            else:
                keys.append(grid)
        return list(map(process, locks)), list(map(process, keys))

def process(grid):
    return tuple(len([s[i:i+1] for s in grid if s[i:i+1] == '#']) - 1 for i in range(5))

def does_fit(lock, key):
    for l, k in zip(lock, key):
        if l + k > 5:
            return False
    return True

@timed
def main():
    locks, keys = get_input('./input.txt')
    matches = 0
    for key in keys:
        for lock in locks:
            if does_fit(lock, key): matches += 1
    print(matches)

if __name__ == "__main__":
    main()
