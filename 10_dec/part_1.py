import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timer
from itertools import product

def get_input(filename):
    with open(filename, 'r') as file:
        return [[int(x) for x in line] for line in file.read().strip().split('\n')]

def is_pos_in_grid(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def get_next_ops(pos):
    x, y = pos
    return[
        (x, y+1),
        (x+1, y),
        (x-1, y),
        (x, y-1)
    ]

def travel_to_top(grid, pos):
    x, y = pos
    if grid[x][y] == 9:
        return [pos]
    options = list(filter(lambda opt: is_pos_in_grid(grid, opt), get_next_ops(pos)))
    unique_tops = []
    for x2, y2 in options:
        if grid[x2][y2] - grid[x][y] == 1:
            unique_tops += travel_to_top(grid, (x2, y2))
    return unique_tops
    
def find_trail_heads(grid):
    trailheads = []
    for x, y in product(range(len(grid)), range(len(grid[0]))):
        if grid[x][y] == 0:
            trailheads.append(travel_to_top(grid, (x, y)))
    return trailheads

def main():
    grid = get_input('./input.txt')
    print(sum(map(lambda heads: len(set(heads)), find_trail_heads(grid))))

if __name__ == "__main__":
    with timer():
        main()
