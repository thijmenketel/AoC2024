import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from itertools import product

def get_input(filename):
    with open(filename, 'r') as file:
        return [line for line in file.read().strip().split('\n')]

def is_pos_in_grid(grid, pos):
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])

def get_next_ops(pos):
    x, y = pos
    return [
        (x, y+1),
        (x+1, y),
        (x-1, y),
        (x, y-1)
    ]

def dfs(grid, pos, visited, name, perimeter):
    if not is_pos_in_grid(grid, pos): return [], perimeter + 1
    x, y = pos
    if grid[x][y] != name: return [], perimeter + 1
    if pos in visited: return [], perimeter
    added = [pos]
    visited += added
    for opt in get_next_ops(pos):
        field, perimeter = dfs(grid, opt, visited, name, perimeter)
        added += field
    return added, perimeter

def find_field(grid, pos):
    x, y = pos
    name = grid[x][y]
    return dfs(grid, pos, [], name, 0)

def find_all_fields(grid):
    fields, visited = [], set()
    for x, y in product(range(len(grid)), range(len(grid[0]))):
        if (x, y) in visited: continue
        field = find_field(grid, (x, y))
        visited.update(field[0])
        fields.append((len(field[0]), field[1]))
    return fields

@timed
def main():
    grid = get_input('./input.txt')
    print(sum(map(lambda x: x[0]*x[1], find_all_fields(grid))))

if __name__ == "__main__":
    main()
