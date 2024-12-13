import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timed
from itertools import product
from part_1 import (
    get_input,
    get_next_ops,
    is_pos_in_grid,
)

def dfs(grid, pos, visited, name):
    if not is_pos_in_grid(grid, pos): return []
    x, y = pos
    if grid[x][y] != name: return []
    if pos in visited: return []
    added = [pos]
    visited += added
    for opt in get_next_ops(pos):
        added += dfs(grid, opt, visited, name)
    return added

def find_field(grid, pos):
    x, y = pos
    name = grid[x][y]
    return dfs(grid, pos, [], name)

def find_perimeter(grid, field, name):
    perimeter = []
    for pos in field:
        x,y = pos
        if not is_pos_in_grid(grid, (x, y - 1)) or grid[x][y - 1] != name:
            perimeter.append((x, y, 'TOP'))
        if not is_pos_in_grid(grid, (x + 1, y)) or grid[x + 1][y] != name:
            perimeter.append((x, y, 'RIGHT'))
        if not is_pos_in_grid(grid, (x, y + 1)) or grid[x][y + 1] != name:
            perimeter.append((x, y, 'BOTTOM'))
        if not is_pos_in_grid(grid, (x - 1, y)) or grid[x - 1][y] != name:
            perimeter.append((x, y, 'LEFT'))
    return perimeter

def count_corners(perimeters):
    corners = 0
    for x, y, side in sorted(perimeters):
        if side in ['LEFT', 'RIGHT'] and (x, y + 1, side) not in perimeters:
            corners += 1
        elif side in ['TOP', 'BOTTOM'] and (x + 1, y, side) not in perimeters:
            corners += 1
    return corners

def find_all_fields(grid):
    fields, sides, visited = [], [], set()
    for x, y in product(range(len(grid)), range(len(grid[0]))):
        if (x, y) in visited: continue
        field = find_field(grid, (x, y))
        visited.update(field)
        fields += [field]
        perimeter = find_perimeter(grid, field, grid[x][y])
        sides.append(count_corners(perimeter))
    return fields, sides

@timed
def main():
    grid = get_input('./input.txt')
    fields, sides = find_all_fields(grid)
    total = sum([len(field) * side for field, side in zip(fields, sides)])
    print(total)

if __name__ == "__main__":
    main()
