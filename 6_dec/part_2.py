import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from util import timer
from copy import deepcopy
from part_1 import (
    get_input,
    turn_right,
    next_pos,
    is_pos_in_grid,
    traverse_grid,
)

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print('*' * len(grid))

def test_grid(grid, pos, dir):
    x, y = next_pos(pos, dir)
    rights = []
    right = None
    while is_pos_in_grid(grid, (x, y)):
        match grid[x][y]:
            case '.'|'^':
                pos = (x, y)
            case '#'|'O':
                if (dir, pos) in rights:
                    return True
                rights.append((dir, pos))
                dir = turn_right(dir)
        x, y = next_pos(pos, dir)
    return False


def find_blocks_in_grid(grid, blocklist):
    dir, start = blocklist[0]
    blocks = []
    for block in blocklist[1:]:
        ndir, (x, y) = block
        if (x, y) not in blocks:
            grid[x][y] = 'O'
            if test_grid(grid, start, dir): 
                blocks += [(x, y)]
            grid[x][y] = '.'
        start = (x, y)
        dir = ndir
    return len(blocks)

def main():
    grid = get_input('./input.txt')
    print(find_blocks_in_grid(grid, traverse_grid(deepcopy(grid))))

if __name__ == "__main__":
    with timer():
        main()