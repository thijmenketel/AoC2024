import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from itertools import permutations
from part_1 import (
    get_input,
    is_pos_in_grid,
    find_antennas,
    get_diff,
    get_antinode_opt
)

def find_antinodes(grid):
    antennas = find_antennas(grid)
    antinodes = set()
    for antenna in antennas:
        for first, second in permutations(antenna, 2):
            diff = get_diff(first, second)
            opt = get_antinode_opt(first, diff)
            while is_pos_in_grid(grid, opt):
                antinodes.add(opt)
                opt = get_antinode_opt(opt, diff)
    return antinodes

@timed
def main():
    grid = get_input('./input.txt')
    print(len(find_antinodes(grid)))

if __name__ == "__main__":
    main()
