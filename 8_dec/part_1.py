import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from itertools import product, permutations

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print('-' * len(grid))

def get_input(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file if line]
    return grid

def find_antennas(grid):
    antennas = {}
    for x, y in product(range(len(grid)), range(len(grid[0]))):
        if grid[x][y] != '.':
            antennas.setdefault(grid[x][y], []).append((x, y))
    return antennas.values()

def is_pos_in_grid(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def get_diff(pos1, pos2):
    return pos2[0] - pos1[0], pos2[1] - pos1[1]

def get_antinode_opt(pos, diff):
    return pos[0] + diff[0], pos[1] + diff[1]

def find_antinodes(grid):
    antennas = find_antennas(grid)
    antinodes = set()
    for antenna in antennas:
        for first, second in permutations(antenna, 2):
            diff = get_diff(first, second)
            opt = get_antinode_opt(second, diff)
            if is_pos_in_grid(grid, opt):
                antinodes.add(opt)
    return antinodes

@timed
def main():
    grid = get_input('./input.txt')
    print(len(find_antinodes(grid)))

if __name__ == "__main__":
    main()
